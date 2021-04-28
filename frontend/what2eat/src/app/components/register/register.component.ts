import { Component, OnInit } from '@angular/core';
import { UserService } from '../../services/user.service';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import { FoodService } from '../../services/food.service';
import { Register, FoodRating, FoodWithRating } from 'src/interface';


@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  public foodinformation : any ;
  isLinear = true;
  registrationFormGroup1!: FormGroup ;
  registrationFormGroup2!: FormGroup ;
  starRating = 0; 
  public ratingList: FoodRating[] = [];

  

  constructor(
    public _userService: UserService , 
    private _formBuilder: FormBuilder,
    private _foodService: FoodService
    ) { }

  ngOnInit(): void {  
    this.registrationFormGroup1 = this._formBuilder.group({
      username: ['', Validators.required],
      password: ['', Validators.required]
    });
    this.registrationFormGroup2 = this._formBuilder.group({
      foodinformation: this.getFoodList()
    });
  }

  register() {
    // submit user for registration
    console.log(this.registrationFormGroup1.value);
  //  this._userService.register(JSON.stringify(this.registrationFormGroup1.value));
    // save the user initial rating
    console.log(this.foodinformation.results);
    this.submitInitialFoodRating();
  }

  submitInitialFoodRating(){
    const registerInfo: Register = {
      username: this.registrationFormGroup1.controls.username.value,
      password: this.registrationFormGroup1.controls.password.value,
      foodRatingList: this.populateFoodRating()
    }
    console.log(registerInfo);
    this._foodService.submitInitialFoodRating(JSON.stringify(registerInfo));
  }
  populateFoodRating() {
    
    for (let i = 0; i< this.foodinformation.results.length; i++){
      let rate: FoodRating = {
        id: this.foodinformation.results[i].id,
        rating: this.foodinformation.results[i].rating
      };
      console.log(rate)
      this.ratingList.push(rate);
    }
    console.log(this.ratingList)
    return this.ratingList;
  }

  getFoodList() {
    this._foodService.getInitialRatinglist().subscribe(
      // the first argument is a function which runs on success
      data => {
        this.foodinformation = data;
        for (let foodpiece of this.foodinformation.results) {
          console.log(foodpiece);
          foodpiece.thumbnail = './assets/images/'+foodpiece.thumbnail+'.jpg'
          foodpiece.rating = 0
        }
      },
      // the second argument is a function which runs on error
      err => console.error(err),
      // the third argument is a function which runs on completion
      () => console.log('done loading posts')
    );
  }

}
