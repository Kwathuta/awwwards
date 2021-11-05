import { Component, OnInit } from '@angular/core';
import { ProjectService } from 'src/app/services/project.service';

@Component({
  selector: 'app-add-project',
  templateUrl: './add-project.component.html',
  styleUrls: ['./add-project.component.css']
})
export class AddProjectComponent implements OnInit {

  title: string = ''
  description: string = ''
  image: any = ''
  url: any = ''

  // form: any = {
  //   title: null,
  //   image: null,
  //   description: null,
  //   url: null,
  // };
  data: any;
  isSuccessful = false;
  isSignUpFailed = false;
  errorMessage = '';

  constructor(private projectService: ProjectService) { }

  postProject() {


    let form = new FormData()
    console.log(this.title);
    form.append("title", this.title)
    form.append("description", this.description)
    form.append("url", this.url)
    form.append("image", this.image)
    this.projectService.postProject(form)
    this.isSuccessful = true;
  }



  // onSubmit() {
  //   const { title, image, description, url } = this.form;
  //   console.log(this.form)
  //   this.projectService.postProject(title, image, description, url).subscribe(response => {
  //     console.log(response);
  //     this.data = response;
  //     this.isSuccessful = true;
  //     this.isSignUpFailed = false;
  //   }, err => {
  //     this.errorMessage = err.error.message;
  //     this.isSignUpFailed = true;
  //   })
  // }

  onImageChange(event: any) {
    this.image = event.target.files[0]
  }


  ngOnInit(): void {
  }

}
