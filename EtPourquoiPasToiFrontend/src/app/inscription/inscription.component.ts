import { Component, Input, OnInit } from '@angular/core';
import { EmailValidator } from '@angular/forms';
import { ConfigService } from '../service/config.service';

@Component({
  selector: 'app-inscription',
  templateUrl: './inscription.component.html',
  styleUrls: ['./inscription.component.scss']
})
export class InscriptionComponent implements OnInit {
  
  
  constructor(private service:ConfigService) { }

  @Input() utilisateur:any;
  email: any;
  password:any;
  nom:any;
  prenom:any;
  typeUtilisateur:any;
    
  ngOnInit(): void {
    this.utilisateur={
      email:'',
      password:'',
      password2:'',
      nom:'',
      prenom:'',
      typeUtilisateur:'Ingénieure ou étudiante ingénieure',
    };
  }
  inscription(){
    var val={email:this.email,password:this.password,password2:this.password,nom:this.nom,prenom:this.prenom,typeUtilisateur:this.typeUtilisateur}  
    this.service.inscriptionBDD(val).subscribe(res=>{alert(res.toString()); //Méthode qui doit renvoyer les éléments du forms à la base de données --> ne marche pas 
    });
  };
  

}
