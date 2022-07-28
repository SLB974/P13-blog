from django.urls import path

from .views import render_article

urlpatterns=[
        path('article/<int:pk>/', render_article, name='article'),

]
