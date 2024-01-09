from django.urls import path
from . import views

urlpatterns = [
    path('', views.ocr_read, name='ocr'),
    path('apply/', views.apply_create, name='apply'),
]