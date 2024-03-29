import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { NavigationBarComponent } from './navigation-bar/navigation-bar.component';
import { InscriptionComponent } from './inscription/inscription.component';
import { FooterComponent } from './footer/footer.component';
import { AppRoutingModule } from './app-routing.module';
import { HomeComponent } from './home/home.component';
import { ConnexionComponent } from './connexion/connexion.component';
import { RechercheTemoignagesComponent } from './recherche-temoignages/recherche-temoignages.component';
import { ProfilComponent } from './profil/profil.component';

import { ConfigService } from './service/config.service';

import { HttpClientModule } from '@angular/common/http';
import { FormsModule,ReactiveFormsModule } from '@angular/forms';
import { TemoignagesComponent } from './temoignages/temoignages.component';
import { TemoignageComponent } from './temoignage/temoignage.component';

@NgModule({
  declarations: [
    AppComponent,
    NavigationBarComponent,
    InscriptionComponent,
    FooterComponent,
    HomeComponent,
    ConnexionComponent,
    RechercheTemoignagesComponent,
    ProfilComponent,
    TemoignagesComponent,
    TemoignageComponent,
  ], /*déclarer les composants ou directives ou pipes */
  imports: [
    BrowserModule,
    AppRoutingModule,
    
    // import HttpClientModule after BrowserModule.
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
],
  exports:[], /*exporter dans d'autres modules */
  providers: [
    ConfigService,
    ], /*déclarer les services */
  bootstrap: [AppComponent] /*spécifier quel est le composant racine dans le module*/
})
export class AppModule { }
