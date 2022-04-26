import { NgModule } from '@angular/core';
import { RouterModule,Routes } from '@angular/router';
import { InscriptionComponent } from './inscription/inscription.component';
import { HomeComponent } from './home/home.component';
import { ConnexionComponent } from './connexion/connexion.component';
import { RechercheTemoignagesComponent } from './recherche-temoignages/recherche-temoignages.component';
import { ProfilComponent } from './profil/profil.component';
import { TemoignagesComponent } from './temoignages/temoignages.component';

const routes:Routes=[
  {path:'',component:HomeComponent},
  {path:'inscription',component:InscriptionComponent},
  {path:'connexion',component:ConnexionComponent},
  {path:'temoignages',component:RechercheTemoignagesComponent},
  {path:'profil',component:ProfilComponent},
  {path:'listeTemoignages',component:TemoignagesComponent},
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes)
  ]
 ,
exports:[RouterModule] 
})
export class AppRoutingModule { }
