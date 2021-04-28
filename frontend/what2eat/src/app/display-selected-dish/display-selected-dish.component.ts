import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Food, FoodRating} from 'src/interface';
import { FoodService } from '../services/food.service';

@Component({
  selector: 'app-display-selected-dish',
  templateUrl: './display-selected-dish.component.html',
  styleUrls: ['./display-selected-dish.component.css']
})
export class DisplaySelectedDishComponent implements OnInit {

  food!:Food;
  showRecipe: boolean = false;
  showInstruction: boolean = false;

  constructor(
    private router: Router,
    private _foodService: FoodService,
  ) { }

  ngOnInit(): void {
    // get the value 
    this.food = this._foodService.selectedDish;
  }

  showDetails(click: number){
    if (click == 1){
      this.showRecipe = true;
      this.showInstruction = false;
    } 
    if (click == 2){
      this.showRecipe = false;
      this.showInstruction = true;
    } 
    if (click == 3){
      this.showRecipe = false;
      this.showInstruction = true;
    } 
  }

  searchInGoogle(){
    window.open("https://www.google.com/search?q=where+to+find+ "+this.food.title);
  }

  stepBack(){
    this.router.navigate(["/recommendationList"]);
  }

  rate(){

    this.router.navigate(["/rateADish"]);
  }

}
