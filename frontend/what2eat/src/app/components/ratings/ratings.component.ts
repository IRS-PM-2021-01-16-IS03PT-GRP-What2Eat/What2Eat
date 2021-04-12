import { Component, OnInit } from '@angular/core';
import { FoodService } from '../../services/food.service';

@Component({
  selector: 'app-ratings',
  templateUrl: './ratings.component.html',
  styleUrls: ['./ratings.component.css']
})
export class RatingsComponent implements OnInit {

  public foodinformation : any;
  constructor(private _foodService: FoodService) { 

  }

  ngOnInit(): void {
    this.getFood();
  }
  
  getFood() {
    this._foodService.list().subscribe(
      // the first argument is a function which runs on success
      data => {
        this.foodinformation = data;
        for (let foodpiece of this.foodinformation.results) {
          foodpiece.thumbnail = './assets/images/'+foodpiece.thumbnail+'.jpg'
        }
      },
      // the second argument is a function which runs on error
      err => console.error(err),
      // the third argument is a function which runs on completion
      () => console.log('done loading posts')
    );
  }
  

}
