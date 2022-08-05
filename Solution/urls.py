from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("showVideos/", views.showVideos, name="showVideos"),
    path("validate/", views.validate, name="validate"),
    path("putVideo/", views.FileUploadView.as_view(), name="putVideo"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
