#coding=utf-8
from libs.globals import globals

def globals_processor(request):
    return {'globals': globals}



menu = [
        ('/', u'Главная', None),
#        ('/news/', u'Новости', None),
        ('/about/', u'О компании', [
                                        ('/about/mission/', u'Миссия и цели', None),
#                                        ('/about/sklad/', u'Складской комплекс', None),
                                        ('/about/personal/', u'Сотрудники', None),
                                        ('/about/work/', u'Вакансии', None),
                                   ]),
        ('/catalog/', u'Продукция', [
                                        ('/catalog/new/', u'Новинки', None),
                                        ('/catalog/search/', u'Поиск', None),
#                                        ('/catalog/order/', u'Корзина', None),
                                        ('/catalog/', u'Каталог продукции', None),
                                    ]),
        ('/info/', u'Тех. информация', [
#                                        ('/info/proizv/', u'Производители', None),
#                                        ('/info/', u'Техническая информация', None),
                                    ]),
        ('/order/', u'Заказ', None),
        ('/contacts/', u'Контакты', None),
        ('/media/uploads/price/price.zip', u'Прайс-лист', None),
        ]

def navigation_parse(data, path):
    cur_item = None
    menu = []
    if data and data[2]:
        for item in data[2]:
            if item[0] == '/':
                if path == item[0]:
                    cur_item = item
                    menu.append((item[0],True,item[1]))
                else:
                    menu.append((item[0],False,item[1]))    
            elif not cur_item and path.startswith(item[0]):
                cur_item = item
                menu.append((item[0],True,item[1]))
            else:
                menu.append((item[0],False,item[1]))    
    return cur_item, menu

def navigation_processor(request):
    
    item0 = ['','',menu]
    item1, menu1 = navigation_parse(item0, request.path)
    item2, menu2 = navigation_parse(item1, request.path)
    
    breadcrumbs = [('/', False, u'Главная')]
    if item1 and item1[0]!=request.path: breadcrumbs.append((item1[0],True,item1[1]))
    if item2 and item2[0]!=request.path: breadcrumbs.append((item2[0],True,item2[1]))
#    if not item2 and len(breadcrumbs)==1: breadcrumbs = []
     
    return {'menu1': menu1, 'menu2': menu2, 'breadcrumbs': breadcrumbs}
    

#def basket_processor(request):
#    return {'basket_data': request.session.get('basket_data', '')}
