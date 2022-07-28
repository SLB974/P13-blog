from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("category/", views.category_list, name="category_list"),
    path("category/<str:category>/", views.category, name="category"),
    path("article/", views.article_list, name="article_list"),
    path("article/<str:title>/", views.article, name="article"),
    path("tutorial/", views.tuto_list, name="tuto_list"),
    path("tutorial/<str:title>/", views.tuto, name="tuto"),
    path("oops/", views.oops_list, name="oops_list"),
    path("oops/<str:title>/", views.oops, name="oops"),
    
]
