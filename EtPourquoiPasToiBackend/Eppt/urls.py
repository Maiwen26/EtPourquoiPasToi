from django.urls import re_path as url
from Eppt import views

urlpatterns=[url(r'^temoignage/$',views.temoignageAPI),
url(r'^temoignage/([0-9]+)$',views.temoignageAPI)]