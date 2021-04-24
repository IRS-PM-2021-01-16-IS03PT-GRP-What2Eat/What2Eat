import { Component, OnInit } from '@angular/core';
import { FoodService } from '../services/food.service';


@Component({
  selector: 'app-daily-recommend',
  templateUrl: './daily-recommend.component.html',
  styleUrls: ['./daily-recommend.component.css']
})
export class DailyRecommendComponent implements OnInit {

  
  constructor(
    private _foodService: FoodService
  ) { }
  

  ngOnInit(): void {
  }

  searchDish(choice: number){
    console.log(choice)
  }

  picky(){
    
  }

}
