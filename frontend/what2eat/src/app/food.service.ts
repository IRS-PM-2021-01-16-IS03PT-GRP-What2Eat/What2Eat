import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class FoodService {

  constructor(private http: HttpClient) { }

  // Uses http.get() to load data from a single API endpoint
  list() {
    // let httpOptions = {
    //   headers: new HttpHeaders({
    //     'Content-Type': 'application/json',
    //     'Authorization': 'Bearer ' + localStorage.getItem('access')   
    //   })
    // };
    // return this.http.get('/api/food/', httpOptions);
    return this.http.get('/api/food/');
  }
}
