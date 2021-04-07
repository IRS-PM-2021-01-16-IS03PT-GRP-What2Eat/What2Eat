import { Component, OnInit } from '@angular/core';
import { FoodService } from '../../services/food.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-food-information',
  templateUrl: './food-information.component.html',
  styleUrls: ['./food-information.component.css']
})
export class FoodInformationComponent implements OnInit {
  
  public foodinformation : any;
  constructor(private _foodService: FoodService, private route: ActivatedRoute) { 

  }

  ngOnInit(): void {
    const foodid = this.route.snapshot.paramMap.get('id') || '';
    this.getFood(foodid);
  }

  getFood(foodid: string) {
    this._foodService.listDetail(foodid).subscribe(
      // the first argument is a function which runs on success
      data => {
        this.foodinformation = data;
        this.foodinformation.thumbnail = './assets/images/'+this.foodinformation.thumbnail+'.jpg'
      },
      // the second argument is a function which runs on error
      err => console.error(err),
      // the third argument is a function which runs on completion
      () => console.log('done loading posts')
    );
  }
  

}
