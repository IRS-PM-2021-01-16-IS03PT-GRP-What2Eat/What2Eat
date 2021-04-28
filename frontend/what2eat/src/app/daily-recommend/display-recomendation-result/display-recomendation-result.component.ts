import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Food} from 'src/interface';
import { FoodService } from '../../services/food.service';

@Component({
  selector: 'app-display-recomendation-result',
  templateUrl: './display-recomendation-result.component.html',
  styleUrls: ['./display-recomendation-result.component.css']
})
export class DisplayRecomendationResultComponent implements OnInit {

  foodList!: Food[];
  constructor(
    private router: Router,
    private _foodService: FoodService,
    ) {
    // const navigation = this.router.getCurrentNavigation();
    // if (navigation != null){
    //   const state = navigation.extras.state as {foodData: Food[]};
    //   this.foodList = state.foodData;
    //   for (let foodpiece of this.foodList) {
    //     foodpiece.thumbnail = './assets/images/'+foodpiece.thumbnail+'.jpg'
    //   }
    // }
  }


  ngOnInit(): void {
    console.log("print no on init")
    this.foodList = this._foodService.recommendedDish;
    console.log(this.foodList)
    for (let foodpiece of this.foodList) {
      if (!foodpiece.thumbnail.includes('./assets/images/')){
        foodpiece.thumbnail = './assets/images/'+foodpiece.thumbnail+'.jpg'
      }
    }
  }

  goToDishPage(food: Food ){
    // store the value in service
    this._foodService.selectedDish = food;
    this.router.navigate(["/selectedDish"]);
  }

}
