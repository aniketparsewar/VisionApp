from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.landing, name='landing'),
    path('image_upload', views.image_view, name = 'image_upload'),
    path('msft_vision', views.msft_vision, name = 'msft_vision'),
    path('msft_index', views.msft_index, name = 'msft_index'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)