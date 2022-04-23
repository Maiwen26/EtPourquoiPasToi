from django.urls import path
from Eppt.views import temoignageDetails, temoignageModification, temoignageSuppression, temoignageCreation

urlpatterns=[
    #url(r'^temoignage/$',views.temoignageAPI),
    #url(r'^temoignage/([0-9]+)$',views.temoignageAPI),
    #url(r'^register',views.utilisateurAPI),
    #url(r'^login',obtain_auth_token)
    path('<slug>/',temoignageDetails,name="detail"),
    path('<slug>/modification',temoignageModification,name="modification"),
    path('<slug>/suppression',temoignageSuppression,name="suppression"),
    path('creation',temoignageCreation,name="creation"),
]