import { Component, OnInit } from '@angular/core';
import { ProjectService } from 'src/app/services/project.service';

@Component({
  selector: 'app-add-project',
  templateUrl: './add-project.component.html',
  styleUrls: ['./add-project.component.css']
})
export class AddProjectComponent implements OnInit {

  form: any = {
    title: null,
    image: null,
    description: null,
    url: null,
  };
  data: any;
  isSuccessful = false;
  isSignUpFailed = false;
  errorMessage = '';

  constructor(private projectService: ProjectService) { }

  onSubmit() {
    const { title, image, description, url } = this.form;
    console.log(this.form)
    this.projectService.postProject(title, image, description, url).subscribe(response => {
      console.log(response);
      this.data = response;
      this.isSuccessful = true;
      this.isSignUpFailed = false;
    }, err => {
      this.errorMessage = err.error.message;
      this.isSignUpFailed = true;
    })
  }

  ngOnInit(): void {
  }

}
