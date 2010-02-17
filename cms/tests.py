"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from djanym.cms.models import Page 
from djanym.cms.constants import * 

class SimpleTest(TestCase):
    def setUp(self):
        self.page1 = Page.objects.create(slug="", name="Home page", type=PAGE_TYPE_STATIC, sort=1)
        self.page2 = Page.objects.create(slug="about", 
                                         name="About", 
                                         title="About company", 
                                         type=PAGE_TYPE_STATIC,
                                         sort=2)
        self.page3 = Page.objects.create(slug="history", 
                                         name="History", 
                                         type=PAGE_TYPE_STATIC,
                                         status=STATUS_HIDDEN, 
                                         parent=self.page2)
        # Need reloading data, because eath children saving modified parents data
        self.page2 = Page.objects.get(id=2)
        self.page4 = Page.objects.create(slug="company", 
                                         name="Company", 
                                         type=PAGE_TYPE_STATIC,
                                         sort=3)
        
    def test_creation(self):
        self.assertEquals(self.page1.title, 'Home page')
        self.assertEquals(self.page1.url, '')
        self.assertEquals(self.page1.get_absolute_url(), '/')
        self.assertEquals(self.page2.title, 'About company')
        self.assertEquals(self.page2.url, 'about')
        self.assertEquals(self.page2.get_absolute_url(), '/about/')
        self.assertEquals(self.page3.url, 'about/history')
        self.assertEquals(self.page3.__unicode__(), '-- History')
        self.assertEquals(list(Page.active_objects.all()), 
                          [self.page1, self.page2, self.page4] )

    def test_modify_url(self):
        self.page2.slug = 'about_company'
        self.page2.save()
        self.page3 = Page.objects.get(id=3)
        self.assertEquals(self.page3.url, 'about_company/history')

    def test_modify_parent(self):
        self.page2.parent = self.page4
        self.page2.save()
        self.page3 = Page.objects.get(id=3)
        self.assertEquals(self.page3.url, 'company/about/history')
        
        
__test__ = {"doctest": """
"""}


#>>> from djanym.cms.models import Page 
#>>> from djanym.cms.constants import * 
#>>> page1 = Page.objects.create(slug="", name="Home page", type=PAGE_TYPE_STATIC)
#>>> page1.url
#''
#>>> page1.title
#'Home page'
#>>> page1.get_absolute_url()
#'/'
#>>> page1 = Page.objects.create(slug="about", name="About", title="About company", type=PAGE_TYPE_STATIC, parent=page1)
#>>> page1.title
#'About company'
