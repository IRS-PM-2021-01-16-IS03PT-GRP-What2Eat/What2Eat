import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Food, FoodWithRating } from 'src/interface';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})

export class FoodService {

  private httpOptions: any;
  recommendedDish:Food[] = [];
  selectedDish:any;
  constructor(private http: HttpClient) { 
    this.httpOptions = {
      headers: new HttpHeaders({'Content-Type': 'application/json'})
    };
  }

  // Uses http.get() to load data from a single API endpoint
  list(): Observable<Food[]> {
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

  getInitialRatinglist(): Observable<FoodWithRating[]> {
    let httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        //  'Authorization': 'Bearer ' + localStorage.getItem('access')   
      })
    };
    return this.http.get<FoodWithRating[]>('/api/register/initialFoodRating/', httpOptions).pipe(map(res => res));
  }

  searchDish(choice: number): Observable<any> {
    let httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        //  'Authorization': 'Bearer ' + localStorage.getItem('access')   
      })
    };
    return this.http.post('/api/dailyRecommend/', JSON.stringify({"choice":choice}), httpOptions);
  }

  submitInitialFoodRating(ratings: string){
    console.log("save initial rating")
    this.http.post('/api/register/saveInitialRating/', ratings, this.httpOptions).subscribe(
      data => {
      //  this.updateRegisterData(data)
      },
      err => {
     //   this.errors = err['error'];
      }
    );
    // let httpOptions = {
    //   headers: new HttpHeaders({
    //     'Content-Type': 'application/json',
    //     //  'Authorization': 'Bearer ' + localStorage.getItem('access')   
    //   })
    // };
    console.log("here")
    // return this.http.post('api/register/saveInitialRating/', ratings, httpOptions);
  }

  submitFoodRating(ratings: string){
    console.log(ratings)
    console.log("submitFoodRating")
    // this.http.post('/api/rateADish/', ratings, this.httpOptions)

    this.http.post('/api/rateADish/', ratings, this.httpOptions).subscribe(
      data => {
      //  this.updateRegisterData(data)
      },
      err => {
     //   this.errors = err['error'];
      }
    );
  }
}
