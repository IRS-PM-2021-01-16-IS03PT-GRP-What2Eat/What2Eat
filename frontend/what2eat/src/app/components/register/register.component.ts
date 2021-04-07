import { Component, OnInit } from '@angular/core';
import { UserService } from '../../services/user.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  public user: any;

  constructor(public _userService: UserService) { }

  ngOnInit(): void {
    this.user = {
      username: '',
      password: ''
    };
  }

  register() {
    this._userService.register(JSON.stringify({'username': this.user.username, 'password': this.user.password}));
  }

}
