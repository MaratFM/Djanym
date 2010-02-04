#coding=utf-8
import datetime
import random
import re

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db import transaction
from django.template.loader import render_to_string
from django.utils.hashcompat import sha_constructor
from django.utils.translation import ugettext_lazy as _



from django.contrib.auth.models import User
from registration.models import RegistrationProfile, RegistrationManager

class Accaunt(User, RegistrationProfile):


    # Use UserManager to get the create_user method, etc.
    objects = RegistrationManager()
