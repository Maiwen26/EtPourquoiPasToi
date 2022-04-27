import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ConfigService {
  // Lien avec l'url principal du backend
readonly APIUrl="http://127.0.0.1:8000/";
//Lien avec le dossier média dans lequel se trouve le contenu de chaque témoignage
readonly mediasUrl="http://127.0.0.1:8000/media/"
  constructor(private http:HttpClient) { }

  // Réceupération des urls liés aux témoignages :
  listeTemoignage():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl+'liste');
  }

  ajouterTemoignage(val:any){
    return this.http.post(this.APIUrl+'creation',val);
  }

  modifierTemoignage(val:any){
    return this.http.put(this.APIUrl+'<temoignageId>/modification',val);
  }

  suppressionTemoignage(val:any){
    return this.http.delete(this.APIUrl+'<temoignageId>/suppression',val)
  }


  // Réceupération des urls liés aux utilisateurs :
  vueProfil(val:any){
    return this.http.get(this.APIUrl+'monProfil',val);
  }

  modifierProfil(val:any){
    return this.http.put(this.APIUrl+'monProfil/modification',val);
  }

  suppressionProfil(val:any){
    return this.http.delete(this.APIUrl+'monProfil/suppression',val)
  }

  inscriptionBDD(val:any){
    return this.http.post(this.APIUrl+'inscription',val);
  }



}
