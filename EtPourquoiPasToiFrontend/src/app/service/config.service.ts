import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable()
export class ConfigService {
readonly APIUrl="http://127.0.0.1:8000/";


  constructor(private http: HttpClient) { }

  getTemList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl+'/temoignage');
  }

  addTem(val:any){
    return this.http.post<any[]>(this.APIUrl+'/temoignage',val);
  }

  updateTem(val:any){
    return this.http.put<any[]>(this.APIUrl+'/temoignage',val);
  }

  deleteTem(val:any){
    return this.http.delete<any[]>(this.APIUrl+'/temoignage',val);
  }

}
