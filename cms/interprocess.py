#coding=utf-8
import threading
import time
from djanym.libs.globals import globals
import os
import mmap
from constants import IP_KEYS_LEN

def log_threaded(s):
    '''
    Выводит служебную информацию в консоль с добавлением сведений о текущем процессе и потоке
    '''
    # нельзя ничего выводить для прохождения тестов
    pass
#    print '%-40s #%4s (%s)' % (s, os.getpid(), threading.currentThread().getName())


class InterProcess(object):
    '''
    Класс для межпроцессного взаимодействия
    создает участок распределнной памяти и помещает в него версии ключей
    ключи - числа от 0 до n, где n - номер максимального ключа
    ключи должны быть по порядку начиная с 0, например 0,1,2,3,... и т.д.
    
    версии помещаются для того, чтобы любой процесс/поток мог сравнить
    версию ключа в свой памяти и версию в разделяемой памяти и при несоответствии
    произвести обновление (после чего сохранить версию из разделяемой памяти в своей)
    
    функции clear_key и clear_all записывают новые версии ключей в разделяемую память
    тем самым заставляя все процессы/потоки обновится при следующей проверке.  
     
    '''
    FORMAT_LEN = 25
    
    def __init__(self, keys_len):
        self.keys_len = keys_len
        self._mmap = mmap.mmap(-1, self.keys_len*self.FORMAT_LEN)

    def _format_version(self):
        return '%025.10f' % time.time()

    def clear_key(self, key=0):
        log_threaded('Clear cache #%s' % key)
        self._mmap.seek(key*self.FORMAT_LEN)
        self._mmap.write(self._format_version())
                
    def clear_all(self):
        map(self.clear_cache, xrange(self.keys_len))

    def get_version(self, key=0):
        self._mmap.seek(key*self.FORMAT_LEN)
        return self._mmap.read(self.FORMAT_LEN) 

    def comp_globals(self, key=0):
        '''
        Функция проверяет соответствие переменной в globals и текущей версией
        ключа в резделяемой памяти
        возвращает:
                    True - если соответствуют, обновление не нужно 
                    False - версия поменялась, нужно обновится
        '''
        attr_name = 'ip_ver_%s' % key
        fact_ver = getattr(globals, attr_name, '')
        need_ver = self.get_version(key)
        if not fact_ver or fact_ver!=need_ver:
            setattr(globals, attr_name, need_ver)
            return False
        else:
            return True

interprocess = InterProcess(IP_KEYS_LEN)
