import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable()
export class ConfigService {
readonly APIUrl="http://127.0.0.1:8000/";
readonly DocumentUrl="http://127.0.0.1:8000/media/medias"


  constructor(private http: HttpClient) { }

  //Lien entre backend et frontend des différentes méthodes pour les témoignages :
  temoignage():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl+'monProfil');
  }

  ajoutTemoignage(val:any){
    return this.http.post<any[]>(this.APIUrl+'creation',val);
  }

  modificationTemoignage(val:any){
    return this.http.put<any[]>(this.APIUrl+'<temoignageId>/modification',val);
  }

  suppressionTemoignage(val:any){
    return this.http.delete<any[]>(this.APIUrl+'<temoignageId>/suppression',val);
  }

  listeTemoignage(){
    return this.http.get<any[]>(this.APIUrl+'liste')
  }

 //Lien entre backend et frontend des différentes méthodes pour les utilisateurs :
  utilisateur():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl+'monProfil');
  }

  ajoutUtilisateur(val:any){
    return this.http.post<any[]>(this.APIUrl+'inscription',val);
  }

  modificationUtilisateur(val:any){
    return this.http.put<any[]>(this.APIUrl+'monProfil/modification',val);
  }

  suppressionUtilisateur(val:any){
    return this.http.delete<any[]>(this.APIUrl+'monProfil/suppression',val);
  }

}
