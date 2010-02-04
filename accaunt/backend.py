from django.conf import settings
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site
import re
from registration import signals
from forms import RegistrationForm
from registration.custom_user import User
from registration.backends.default import DefaultBackend

USERNAME_RE = re.compile('\W+')

class EmployerBackend(DefaultBackend):

    def register(self, request, **kwargs):
        first_name, last_name, email, password = kwargs['first_name'], kwargs['last_name'], kwargs['email'], kwargs['password1']
        
        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)
        
        username = USERNAME_RE.sub('_', email)
        while User.objects.filter(username__iexact=username):
            username = username+'_'         
        
        new_user = User.objects.create_inactive_user(username, email, password, site)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()
        
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)
        return new_user

    def get_form_class(self, request):
        """
        Return the default form class used for user registration.
        
        """
        return RegistrationForm
