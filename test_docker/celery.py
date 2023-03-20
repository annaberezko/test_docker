import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_docker.settings')

app = Celery('test_docker')
app.config_from_object('django_conf:settings', namespace='CELERY')
app.autodiscover_tasks()
