"""_summary_
"""
from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import signup

urlpatterns=[
    path("account/signup", signup, name="signup"),
    path("account/logout", LogoutView.as_view(), name="logout"),
]
