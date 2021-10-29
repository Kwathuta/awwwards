import { Component, OnInit } from '@angular/core';
import { ProjectService } from 'src/app/services/project.service';
import { IProject } from 'src/app/interfaces/project';

@Component({
  selector: 'app-projects',
  templateUrl: './projects.component.html',
  styleUrls: ['./projects.component.css']
})
export class ProjectsComponent implements OnInit {
  projects: IProject[] = []

  constructor(private projectService: ProjectService) { }

  getProjects() {
    this.projectService.getProjects().subscribe((response: any) => {
      this.projects = response;
      console.log(this.projects)
    })
  }

  ngOnInit(): void {
    this.getProjects();
  }

}
