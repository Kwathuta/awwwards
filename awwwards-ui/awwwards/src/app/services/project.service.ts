import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ProjectService {

  constructor(private http: HttpClient) {
    console.log('Starting service')
  }

  getProjects() {
    return this.http.get(`${environment.BASE_URL}projects/`)
  }

  postProject() {
    return this.http.get(`${environment.BASE_URL}projects/`)
  }

  getProject(projectId: number) {
    return this.http.get(`${environment.BASE_URL}projects/${projectId}`)
  }
}
