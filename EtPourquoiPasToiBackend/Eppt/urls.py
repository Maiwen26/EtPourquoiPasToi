from django.urls import path
from Eppt.views import temoignageDetails, temoignageModification, temoignageSuppression, temoignageCreation, inscription,ListeTemoignage,vueProfil,modificationProfil,suppressionProfil

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    path('<temoignageId>/',temoignageDetails,name="detail"),
    path('<temoignageId>/modification',temoignageModification,name="modification"),
    path('<temoignageId>/suppression',temoignageSuppression,name="suppression"),
    path('creation',temoignageCreation,name="creation"),

    path('inscription',inscription,name="inscription"),
    path('connexion',obtain_auth_token,name="login"),
    path('monProfil',vueProfil,name='monProfil'),
    path('monProfil/modification',modificationProfil,name='modificationProfil'),
    path('monProfil/suppression',suppressionProfil,name='suppressionProfil'),

    path('liste',ListeTemoignage.as_view(),name='liste'),
]