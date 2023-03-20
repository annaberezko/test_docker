import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_docker.settings')

app = Celery('test_docker')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'print-text-every-1-minutes': {
        'task': 'testapp.tasks.print_text',
        'schedule': crontab(minute='*/1')
        # 'schedule': crontab(minute=0, hour=0, day_of_week=1)
    }
}
