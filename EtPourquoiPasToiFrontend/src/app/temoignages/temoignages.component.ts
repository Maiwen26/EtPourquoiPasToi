import { Component, OnInit } from '@angular/core';
import { ConfigService } from '../service/config.service';

@Component({
  selector: 'app-temoignages',
  templateUrl: './temoignages.component.html',
  styleUrls: ['./temoignages.component.scss']
})
export class TemoignagesComponent implements OnInit {
  service: any;

  constructor() { }

  Temoignage:any=[];


  ngOnInit(): void {
    this.TemoignageRefresh();
  }

    TemoignageRefresh(){
      this.service.temoignage().subscribe((data: any)=>{
        this.Temoignage=data;
      })
    }
}
