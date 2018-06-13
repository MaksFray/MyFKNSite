import os
import celery
from celery import Celery

print(celery.__file__)
from django.conf import settings
# Основыне настройки Django для celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyFKNSite.settings')
app = Celery('MyFKNSite')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)