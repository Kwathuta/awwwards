import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  form: any = {
    username: null,
    password: null,
    password_confirm: null,
  };
  isSuccessful = false;
  isSignUpFailed = false;
  errorMessage = '';

  constructor(private authService: AuthService) { }

  onSubmit() {
    const { username, password, password_confirm } = this.form;
    console.log(this.form)
    this.authService.register(username, password, password_confirm).subscribe(data => {
      console.log(data);
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
