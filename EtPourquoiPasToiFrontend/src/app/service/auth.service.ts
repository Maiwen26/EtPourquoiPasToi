import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
const AUTH_API = 'http://127.0.0.1:8000/';
const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};
@Injectable({
  providedIn: 'root'
})
export class AuthService {
  constructor(private http: HttpClient) { }
  authToken(credit: { email: any; password: any; }): Observable<any> {
    return this.http.post(AUTH_API + 'authToken', {
      email: credit.email,
      password: credit.password
    }, httpOptions);
  }

}