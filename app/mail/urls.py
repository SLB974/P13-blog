from django.urls import path

from . import views

urlpatterns=[
    path("send_mail/", views.mail_me, name="mail_me"),
    path("mail_sent/", views.mail_sent, name="mail_sent"),
    path("mail_error/", views.mail_error, name="mail_error"),
    
]
