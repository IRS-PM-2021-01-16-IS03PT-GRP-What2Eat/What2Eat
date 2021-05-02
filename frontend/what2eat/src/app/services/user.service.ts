import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})

export class UserService {

   // http options used for making API calls
   private httpOptions: any;
 
   // the actual JWT token
   public token: string

  // the actual JWT token
  public refreshtoken: string
  
   // the token expiration date
   public token_expires: Date;
  
   // the username of the logged in user
   public username: string;
  
   // error messages received from the login attempt
   public errors: any = [];



   constructor(private http: HttpClient, private route: Router) {
     this.httpOptions = {
       headers: new HttpHeaders({'Content-Type': 'application/json'})
     };
     this.token = "";
     this.refreshtoken = "";
     this.token_expires = new Date();
     this.username = "";
   }
  
   // Uses http.post() to get an auth token from djangorestframework-jwt endpoint
   public login(user : string) {
     this.http.post('/api/token/', user, this.httpOptions).subscribe(
       data => {
         this.updateData(data, user);
       },
       err => {
         this.errors = err['error'];
       }
     );
   }

   // Refreshes the JWT token, to extend the time the user is logged in
   public refreshToken() {
     this.http.post('/api/token/refresh/', JSON.stringify({refresh: localStorage.getItem('refresh')}), this.httpOptions).subscribe(
       data => {
         this.updateDataRefresh(data);
       },
       err => {
         this.errors = err['error'];
       }
     );
   }
  
   public logout() {
      this.token = "";
      this.refreshtoken = "";
      this.token_expires = new Date();
      this.username = "";
      localStorage.clear();
      window.location.href = '/';
   }
  
   private updateData(data : any, user: string) {
     this.token = data['access'];
     this.refreshtoken = data['refresh'];
     localStorage.setItem('access', this.token);
     localStorage.setItem('refresh', this.refreshtoken);
     localStorage.setItem('username', JSON.parse(user).username);
     this.username = this.username;
     this.errors = [];
     // decode the token to read the username and expiration timestamp
     const token_parts = this.token.split(/\./);
     const token_decoded = JSON.parse(window.atob(token_parts[1]));
     this.token_expires = new Date(token_decoded.exp * 1000);
     //this.username = token_decoded.user_id;
     window.location.href = '/';
   }

   private updateDataRefresh(data : any) {
    // when we refresh we only get back the access token, so leave refreshtoken unchanged
    this.token = data['access'];
    localStorage.setItem('access', this.token);
    this.errors = [];
    // decode the token to read the username and expiration timestamp
    const token_parts = this.token.split(/\./);
    const token_decoded = JSON.parse(window.atob(token_parts[1]));
    this.token_expires = new Date(token_decoded.exp * 1000);
  };

  public register(register : string) {
    this.http.post('/api/register/', register, this.httpOptions).subscribe(
      data => {
        this.updateRegisterData(data)
      },
      err => {
        this.errors = err['error'];
      }
    );
  }

  private updateRegisterData(data : any) {
    this.username = data['username'];
  }

}

