from django.urls import path

from . import views

urlpatterns=[
    path("category/", views.category_list, name="category_list"),
    path("category/<str:category>/", views.category, name="category"),
    path("list/", views.article_list, name="article_list"),
    path("article/<str:title>/", views.article, name="article"),
    path("delete/<str:title>/", views.delete, name="delete_article"),
    path("tutorial/", views.tuto_list, name="tuto_list"),
    path("oops/", views.oops_list, name="oops_list"),
]
