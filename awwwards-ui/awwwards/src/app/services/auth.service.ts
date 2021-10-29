import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http: HttpClient) { }

  register(username: string, password: string, password_confirm: string): Observable<any> {
    return this.http.post(`${environment.AUTH_URL}register/`, {
      username, password, password_confirm
    }, httpOptions);
  }
}
