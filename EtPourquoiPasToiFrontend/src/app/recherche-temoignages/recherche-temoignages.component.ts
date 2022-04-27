import { Component, OnInit } from '@angular/core';
import { ConfigService } from '../service/config.service';

@Component({
  selector: 'app-recherche-temoignages',
  templateUrl: './recherche-temoignages.component.html',
  styleUrls: ['./recherche-temoignages.component.scss']
})
export class RechercheTemoignagesComponent implements OnInit {

  constructor(private sevice:ConfigService) { }

  ngOnInit(): void {
  }

  RechercheRegion(repForm: any){
    for ( const temoignage in this.sevice.listeTemoignage())
    {
      //if (temoignage.region)    --> pas d'accès au champs du modèle témoignage
    }

  }

  RechercheDomaineEtude(repForm: any){
    
    for ( const temoignage in this.sevice.listeTemoignage())
    {
      //if (temoignage.domaineEtude)    --> pas d'accès au champs du modèle témoignage
    }

    ;
  }

  RechercheType(repForm: any){
    for ( const temoignage in this.sevice.listeTemoignage())
    {
      //if (temoignage.typeTemoignage)    --> pas d'accès au champs du modèle témoignage
    }
  }

}
