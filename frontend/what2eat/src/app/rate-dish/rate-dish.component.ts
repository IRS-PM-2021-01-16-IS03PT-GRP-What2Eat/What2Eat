import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Food, FoodRating, SubmitFoodRating} from 'src/interface';
import { FoodService } from '../services/food.service';
import { UserService } from '../services/user.service';
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
    private _userService: UserService
  ) { }

  ngOnInit(): void {
       // get the value 
       this.food = this._foodService.selectedDish
  }

  submitRating(): void {

    const rates: SubmitFoodRating = {
      username: localStorage.getItem('username'),
      id: this.food.recipe_id,
      rating: this.rating
    }
    this._foodService.submitFoodRating(JSON.stringify(rates));
    //navigate to daily recommend
    this.router.navigate(["/howDoYouFeelToday"]);
  }

  directToDailyRecommendPage(){
    //navigate to daily recommend
    this.router.navigate(["/howDoYouFeelToday"]);
  }
}
