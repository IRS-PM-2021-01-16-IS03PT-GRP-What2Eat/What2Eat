import { Component, OnInit } from '@angular/core';
import { UserService } from './services/user.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
 
  public title: any = 'What2Eat';
  public username: any = "";

  constructor(public _userService: UserService) { }

  ngOnInit(): void {
    if(localStorage.getItem('username')&& localStorage.getItem('access')){
        this.username = localStorage.getItem('username');
    }
  }

  logout(){
    this._userService.logout();
  }
 
}