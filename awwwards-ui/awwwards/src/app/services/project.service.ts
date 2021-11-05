import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { IProject } from '../interfaces/project';

token: sessionStorage.getItem("token")

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json', 'Authorization': 'Token ' + sessionStorage.getItem("token") })
};

@Injectable({
  providedIn: 'root'
})
export class ProjectService {

  constructor(private http: HttpClient) {
    console.log('Starting service')
    console.log(sessionStorage.getItem("token"))
  }

  getProjects() {
    return this.http.get(`${environment.BASE_URL}projects/`)
  }

  getProject(projectId: number) {
    return this.http.get(`${environment.BASE_URL}projects/${projectId}`)
  }

  postProject(project: any) {
    return this.http.post(`${environment.BASE_URL}projects/`, project).subscribe(response => {
      return response
    })
  }
}
