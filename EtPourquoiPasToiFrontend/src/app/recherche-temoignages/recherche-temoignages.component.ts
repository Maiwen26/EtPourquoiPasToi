import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-recherche-temoignages',
  templateUrl: './recherche-temoignages.component.html',
  styleUrls: ['./recherche-temoignages.component.scss']
})
export class RechercheTemoignagesComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  RechercheRegion(repForm: any){
    console.log(repForm);

  }

  RechercheDomaineEtude(repForm: any){
    console.log(repForm);
  }

  RechercheType(repForm: any){
    console.log(repForm);
  }

}
