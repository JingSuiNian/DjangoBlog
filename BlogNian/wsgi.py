"""
WSGI config for BlogNian project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append("/usr/local/lib/python2.7/site-packages/Django-1.7.11-py2.7.egg/")
sys.path.append("/usr/local/lib/python2.7/site-packages/MySQLdb/")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BlogNian.settings")

from django.core.wsgi import get_wsgi_application

if os.environ['mod_wsgi.process_group'] != '':
    import signal

    os.kill(os.getpid(), signal.SIGINT)

application = get_wsgi_application()
