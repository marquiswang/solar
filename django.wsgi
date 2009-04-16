import os
import sys

sys.stdout = sys.stderr

os.environ['DJANGO_SETTINGS_MODULE'] = 'solar.settings'

sys.path.append('/usr/local/django')
sys.path.append('/home/sam/solar2009/')
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


