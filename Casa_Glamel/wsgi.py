"""
WSGI config for Casa_Glamel project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Casa_Glamel.staging")

application = Cling(get_wsgi_application())

from django.core.cache.backends.memcached import BaseMemcachedCache
BaseMemcachedCache.close = lambda self, **kwargs: None