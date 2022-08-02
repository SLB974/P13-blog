"""blog URL Configuration"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from home import errors

urlpatterns = [
    path('admin/', admin.site.urls),
    path("article/", include("article.urls")),
    path("user/", include("user.urls")),
    path("accounts/", include('allauth.urls')),
    path("home/", include("home.urls")),
    path("mail/", include("mail.urls")),
    path('factory/', include("factory.urls")),
    path("", RedirectView.as_view(url="home/", permanent=True)),
    path('404/', errors.error_404_view_handler),
    path('500/', errors.error_500_view_handler),
    path('403/', errors.error_403_view_handler),
    path('400/', errors.error_400_view_handler),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404='home.errors.error_404_view_handler'
handler500='home.errors.error_500_view_handler'
handler403="home.errors.error_403_view_handler"
handler400="home.errors.error_400_view_handler"
