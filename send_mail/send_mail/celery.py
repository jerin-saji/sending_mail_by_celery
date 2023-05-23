import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'send_mail.settings')

app = Celery('send_mail')
app.conf.enable_utc = False  # to change the timezone from utc we are using asia/kolkata timezone
app.conf.update(timezone = 'Asia/Kolkata')


app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery Beat Settings

app.conf.beat_schedule = {
    'send-mail-every-day-at-8':{
        'task':'mail_sender.tasks.send_mail_fun',
        'schedule':crontab(hour=10,minute=14)
        
    }
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')