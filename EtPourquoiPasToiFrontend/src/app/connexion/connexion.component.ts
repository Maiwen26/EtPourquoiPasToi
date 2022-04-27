import { Component, OnInit } from '@angular/core';
import { ConfigService } from '../service/config.service';

@Component({
  selector: 'app-connexion',
  templateUrl: './connexion.component.html',
  styleUrls: ['./connexion.component.scss']
})
export class ConnexionComponent implements OnInit {
  public utilisateur:any;
  constructor(private service:ConfigService) {}

  ngOnInit(): void {
    this.utilisateur={
      email:'',
      password:''
    };
  }
  connexion(){
    this.utilisateur.connexion({'email':this.utilisateur.email,'password':this.utilisateur.password});
  }
  
 
  
}
