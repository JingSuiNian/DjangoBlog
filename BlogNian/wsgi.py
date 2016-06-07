"""
WSGI config for BlogNian project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append("/usr/local/lib/python2.7/site-packages/MySQLdb/")
sys.path.append("/usr/local/lib/python2.7/site-packages/Django-1.7.11-py2.7.egg/")
sys.path.append("/usr/local/lib/python2.7/site-packages/pymysql/")
sys.path.append("/usr/local/lib/python2.7/site-packages/PyMySQL-0.7.4.dist-info/")
sys.path.append("/usr/local/lib/python2.7/site-packages/MySQL_python-1.2.5.dist-info/")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BlogNian.settings")

from django.core.wsgi import get_wsgi_application
import time
import traceback
import signal

# application = get_wsgi_application()
try:
    application = get_wsgi_application()
    print 'WSGI without exception'
except Exception:
    print 'handling WSGI exception'
    # Error loading applications
    if 'mod_wsgi' in sys.modules:
        traceback.print_exc()
        os.kill(os.getpid(), signal.SIGINT)
        time.sleep(2.5)
