import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { NavigationBarComponent } from './navigation-bar/navigation-bar.component';
import { InscriptionComponent } from './inscription/inscription.component';
import { FooterComponent } from './footer/footer.component';
import { AppRoutingModule } from './app-routing.module';
import { HomeComponent } from './home/home.component';


@NgModule({
  declarations: [
    AppComponent,
    NavigationBarComponent,
    InscriptionComponent,
    FooterComponent,
    HomeComponent,
  ], /*déclarer les composants ou directives ou pipes */
  imports: [
    BrowserModule,
    AppRoutingModule,
],
  exports:[], /*exporter dans d'autres modules */
  providers: [], /*déclarer les services */
  bootstrap: [AppComponent] /*spécifier quel est le composant racine dans le module*/
})
export class AppModule { }
