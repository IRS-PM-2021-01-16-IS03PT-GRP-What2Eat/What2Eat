import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import { Food } from 'src/interface';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})

export class FoodService {

  constructor(private http: HttpClient) { }

  // Uses http.get() to load data from a single API endpoint
  list()  {
     let httpOptions = {
       headers: new HttpHeaders({
       'Content-Type': 'application/json',
       'Authorization': 'Bearer ' + localStorage.getItem('access')   
        })
     };
    return this.http.get<Food[]>('/api/food/', httpOptions).pipe(map(res => res));
  }

  // listDetail(foodid : string): Observable<Food> {
  //   return this.http.get<Food>('/api/food/'+foodid).pipe(map(res => res));
  // }
}
