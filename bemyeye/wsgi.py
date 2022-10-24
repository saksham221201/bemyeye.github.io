import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bemyeye.settings")
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
from dj_static import Cling

application = Cling(get_wsgi_application())
application = DjangoWhiteNoise(application)
