#coding=utf-8
IP_KEY_MENU = 0
IP_KEY_URLPATTERNS = 1
IP_KEYS_LEN = 2

PAGE_TYPE_STATIC = 0
PAGE_TYPE_APPLICATION = 1
PAGE_TYPE_REDIRECT = 2
PAGE_TYPE_COPY = 3
PAGE_TYPE_LINK = 4

PAGE_TYPES = (
              (0, u'Статическая страница'),
              (1, u'Приложение'),
              (2, u'Перенаправление'),
              (3, u'Дубликат'),
              (4, u'Ссылка'),
              )

STATUS_HIDDEN = 0
STATUS_ACTIVE = 1
STATUS_CHOICES = (
    (0, 'Скрыт.'),
    (1, 'Активн.'),
)
