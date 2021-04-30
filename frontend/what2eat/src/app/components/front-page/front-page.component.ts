import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-front-page',
  templateUrl: './front-page.component.html',
  styleUrls: ['./front-page.component.css']
})
export class FrontPageComponent implements OnInit {

  public username: any = "";

  constructor(private route: Router) { }

  ngOnInit(): void {
    if(localStorage.getItem('username')&& localStorage.getItem('access')){
      this.username = localStorage.getItem('username');
    }
  }

  getstarted(){
    if(this.username){
      this.route.navigate(['howDoYouFeelToday']);  
    }
    else{
      this.route.navigate(['register']);  
    }
   
  }

}
