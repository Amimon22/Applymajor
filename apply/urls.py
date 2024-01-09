from django.urls import path
from . import views
from .views import Apply_result

urlpatterns = [
    path('ocr/<int:category>/', views.ocr_read, name='ocr_read'),
    path('result/', Apply_result.as_view(), name='apply_result'),
]