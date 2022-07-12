from django.urls import path

from .views import upload_md_file

urlpatterns=[
    path('upload/', upload_md_file, name='upload'),
]
