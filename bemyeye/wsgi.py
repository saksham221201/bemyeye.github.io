import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bemyeye.settings")
from dj_static import Cling

application = Cling(get_wsgi_application())
