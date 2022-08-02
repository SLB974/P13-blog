from django.urls import path

from . import views

urlpatterns=[
    path("send_mail/", views.mail_me, name="mail_me"),
    
]
