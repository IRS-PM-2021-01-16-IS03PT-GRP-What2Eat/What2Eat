import { Component, OnInit } from '@angular/core';
import { FoodService } from '../food.service';

@Component({
  selector: 'app-food-information',
  templateUrl: './food-information.component.html',
  styleUrls: ['./food-information.component.css']
})
export class FoodInformationComponent implements OnInit {
  
  public food : any;
  public foodinformation : any;
  constructor(private _foodService: FoodService) { }

  ngOnInit(): void {
    this.getFood();
  }
  getFood() {
    this._foodService.list().subscribe(
      // the first argument is a function which runs on success
      data => {
        this.food = data;
        this.foodinformation = this.food.results;
        for (let foodpiece of this.food.results) {
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
