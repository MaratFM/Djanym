from django.conf import settings
from django.db.models import get_model


_model = getattr(settings, 'CUSTOM_USER_MODEL', 'auth.User')

User = get_model(*_model.split('.', 2))
