"""
URLconf for registration and activation, using django-registration's
default backend.

If the default behavior of these views is acceptable to you, simply
use a line like this in your root URLconf to set up the default URLs
for registration::

    (r'^accounts/', include('registration.backends.default.urls')),

This will also automatically set up the views in
``django.contrib.auth`` at sensible default locations.

If you'd like to customize the behavior (e.g., by passing extra
arguments to the various views) or split up the URLs, feel free to set
up your own URL patterns for these views instead.

"""


from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from registration.views import activate
from registration.views import register
from views import *

backend = 'accaunt.backend.EmployerBackend'

urlpatterns = patterns('',
                       url(r'^activate/complete/$',
                           direct_to_template,
                           { 'template': 'registration/activation_complete.html' },
                           name='registration_activation_complete'),
                       # Activation keys get matched by \w+ instead of the more specific
                       # [a-fA-F0-9]{40} because a bad activation key should still get to the view;
                       # that way it can return a sensible "invalid key" message instead of a
                       # confusing 404.
                       url(r'^activate/(?P<activation_key>\w+)/$',
                           activate,
                           { 'backend': backend },
                           name='registration_activate'),
                       url(r'^register/complete/$',
                           direct_to_template,
                           { 'template': 'registration/registration_complete.html' },
                           name='registration_complete'),
                       url(r'^register/closed/$',
                           direct_to_template,
                           { 'template': 'registration/registration_closed.html' },
                           name='registration_disallowed'),
                       url(r'^register/$',
                           register,
                           { 'backend': backend },
                           name='registration_register'),
                       (r'', include('registration.auth_urls')),




                       url(r'^company/employer_(?P<object_id>\d+)/edit/$',
                           employer_edit,
                           {},
                           name='company_employer_edit'),

                       url(r'^company/employer_(?P<object_id>\d+)/$',
                           employer_detail,
                           {},
                           name='company_employer_detail'),

                       url(r'^company/employer_add/$',
                           employer_add,
                           {},
                           name='company_employer_add'),

                       url(r'^company/edit/$',
                           company_edit,
                           {},
                           name='company_edit'),

                       url(r'^company/details/$',
                           direct_to_template,
                           { 'template': 'account/company_detail.html' },
                           name='company_detail'),

                       url(r'^company/$',
                           direct_to_template,
                           { 'template': 'account/company_index.html' },
                           name='company_index'),

                       url(r'^edit_profile/$',
                           profile_edit,
                           {},
                           name='profile_edit'),

                       url(r'^$',
                           direct_to_template,
                           { 'template': 'account/index.html' },
                           name='account_index'),
)
