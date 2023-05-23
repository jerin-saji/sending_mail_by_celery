from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from celery import shared_task
from django.conf import settings



import time



@shared_task(bind=True)
def send_mail_fun(self):
    users = get_user_model().objects.all()
    for user in users:
        mail_subject = "Hii this is a test email"
        message = "Hai hello how are you !!.."
        to_email = user.email
        send_mail (
            subject= mail_subject,
            message=message,
            from_email= settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return "DONE"

