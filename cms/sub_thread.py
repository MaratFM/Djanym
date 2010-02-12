import threading
import time
from djanym.libs.globals import globals
import os

def log_threaded(s):
    print '%-40s #%4s (%s)' % (s, os.getpid(), threading.currentThread().getName())

def get_version():
    return '%025.10f' % time.time()

def clear_cache(num=0):
    log_threaded('Clear cache #%s' % num)
    map.seek(num*25)
    map.write(get_version())        

def need_reload(num=0):
    map.seek(num*25)
    attr_name = 'cur_ver_%s' % num
    need = False
    cur_ver = getattr(globals, attr_name, '')
    need_ver = map.read(25) 
    if not cur_ver or need_ver!=cur_ver:
        need = True
        setattr(globals, attr_name, need_ver)    

#    print 'Need reload %s = %s       (%s)' % (attr_name, need, threading.currentThread().name)
    return need

import mmap
map = mmap.mmap(-1, 100)
clear_cache(0)
clear_cache(1)