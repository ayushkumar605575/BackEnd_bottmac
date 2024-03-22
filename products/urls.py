from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_image, name='image_display'),
    path('add/', views.upload_image, name='upload_image'),
]