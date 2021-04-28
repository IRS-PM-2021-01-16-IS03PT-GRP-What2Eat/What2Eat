import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Food, FoodRating} from 'src/interface';
import { FoodService } from '../services/food.service';

@Component({
  selector: 'app-rate-dish',
  templateUrl: './rate-dish.component.html',
  styleUrls: ['./rate-dish.component.css']
})
export class RateDishComponent implements OnInit {
  
  food!:Food;
  rating = 0;
  constructor(
    private router: Router,
    private _foodService: FoodService,
  ) { }

  ngOnInit(): void {
       // get the value 
       this.food = this._foodService.selectedDish
  }

  submitRating(): void {
    const rates: FoodRating = {
      id: this.food.id,
      rating: this.rating
    }
    this._foodService.submitFoodRating(JSON.stringify(rates));

    //navigate to daily recommend
    this.router.navigate(["/howDoYouFeelToday"]);
  }
}
