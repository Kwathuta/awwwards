import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  isSuccessful = false;
  isSignInFailed = false;
  errorMessage = '';

  constructor(private http: HttpClient, private route: Router) { }

  register(username: string, password: string, password_confirm: string): Observable<any> {
    return this.http.post(`${environment.AUTH_URL}register/`, {
      username, password, password_confirm
    }, httpOptions);
  }

  login(login: string, password: string) {
    this.http.post(`${environment.AUTH_URL}login/`, { login, password }).subscribe(response => {
      let token: any = response
      sessionStorage.setItem('token', token['token'])
      this.route.navigate(['projects'])
      this.isSuccessful = true;
      this.isSignInFailed = false;
    }, err => {
      this.errorMessage = err.error.message;
      this.isSignInFailed = true;
    })
  }

  logout() {
    sessionStorage.removeItem('currentUser');
  }
}
