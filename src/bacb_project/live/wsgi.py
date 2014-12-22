import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'bacb3.settings'

from django.core.handlers.wsgi import WSGIHandler

application = WSGIHandler()
