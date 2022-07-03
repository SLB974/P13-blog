"""blog URL Configuration"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("article/", include("article.urls")),
    path("tutorial/", include("tutorial.urls")),
    path("user/", include("user.urls")),
    path("accounts/", include('allauth.urls')),
    path("home/", include("home.urls")),
    path("comment/", include("comment.urls")),
    path("mail/", include("mail.urls")),
    path("", RedirectView.as_view(url="home/", permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


