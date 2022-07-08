from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("category/", views.category, name="category"),
    path("article/", views.article, name="article"),
    path("tutorial/", views.tuto, name="tuto"),
    path("oops/", views.oops, name="oops"),
    
]
