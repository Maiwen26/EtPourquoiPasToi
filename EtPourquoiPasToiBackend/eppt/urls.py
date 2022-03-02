from django.urls import path
from . import views

urlpatterns = [
    path('', views.temoignages_list, name='temoignages_list'),
]