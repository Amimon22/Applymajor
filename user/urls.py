from django.urls import path
from . import views

urlpatterns = [
    path('', views.User, name = "user"),
    path('users/', views.user_detail, name='user_detail'),
]