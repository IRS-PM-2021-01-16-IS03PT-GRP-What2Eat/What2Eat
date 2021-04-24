import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Food} from 'src/interface';

@Component({
  selector: 'app-display-recomendation-result',
  templateUrl: './display-recomendation-result.component.html',
  styleUrls: ['./display-recomendation-result.component.css']
})
export class DisplayRecomendationResultComponent implements OnInit {

  foodList!: Food[];
  constructor(private router: Router) {
    const navigation = this.router.getCurrentNavigation();
    if (navigation != null){
      const state = navigation.extras.state as {foodData: Food[]};
      this.foodList = state.foodData;
      for (let foodpiece of this.foodList) {
        foodpiece.thumbnail = './assets/images/'+foodpiece.thumbnail+'.jpg'
      }
    }
  }


  ngOnInit(): void {
    
  }

}
