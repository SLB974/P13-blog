import sys
from imp import reload

from django.conf import settings


def reload_urlconf(urlconf=None):
    if not urlconf:
        urlconf=settings.ROOt_URLCONF
    if urlconf in sys.modules:
        reload(sys.modules[urlconf])

    