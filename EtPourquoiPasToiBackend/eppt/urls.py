from django.urls import path
from .views import (
    TemoignageDetailApiView,
    TemoignageListApiView,
)

urlpatterns = [
    path('api', TemoignageListApiView.as_view()),
    
    path('api/<int:temoignage_id>/', TemoignageDetailApiView.as_view()),
]