from django.shortcuts import render
from .tasks import send_mail_fun
from django.http import HttpResponse



def send_mail_to_all(request):
    send_mail_fun.delay()
    return HttpResponse("Mail has sent")


