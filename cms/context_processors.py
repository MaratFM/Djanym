#coding=utf-8
from djanym.libs.globals import globals

def navigation_processor(request):
    '''
    Processor добавляющий переменные, необходимые для вывода менб и навигации в шаблонах
    '''
    return {'menu': globals.menu_tree, 'page': globals.page, 'breadcrumbs': globals.breadcrumbs}