import { Component, OnInit } from '@angular/core';
import { FoodService } from '../services/food.service';
import { Router } from '@angular/router';
import { Food} from 'src/interface';

@Component({
  selector: 'app-daily-recommend',
  templateUrl: './daily-recommend.component.html',
  styleUrls: ['./daily-recommend.component.css']
})
export class DailyRecommendComponent implements OnInit {

  foodlist!: Food[];

  constructor(
    private _foodService: FoodService,
    private router: Router
  ) { }

  ngOnInit(): void {
  }

  searchDish(choice: number){
    console.log(choice)
    this._foodService.searchDish(choice).subscribe(
      data => {
        console.log()
        this.foodlist = data;
        // store the recommand list to food service
        this._foodService.recommendedDish = this.foodlist;
        this.router.navigate(["/recommendationList"],{state: {foodData: this.foodlist}});
      }
    );

  }

  picky(){

  }

}
