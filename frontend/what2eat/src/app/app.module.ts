import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { HttpClientModule } from '@angular/common/http';  
import { FormsModule, ReactiveFormsModule } from '@angular/forms';   
import { UserService } from './services/user.service';
import { FoodInformationComponent } from './components/food-information/food-information.component';
import { FrontPageComponent } from './components/front-page/front-page.component';
import { LoginComponent } from './components/login/login.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';  
import { MaterialModule } from './materials/material-module';
import { RegisterComponent } from './components/register/register.component';
import { RatingsComponent } from './components/ratings/ratings.component';
import {MatStepperModule} from '@angular/material/stepper';
import {MatInputModule} from '@angular/material/input';
import {MatButtonModule} from '@angular/material/button';
import {MatListModule} from '@angular/material/list';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { DailyRecommendComponent } from './daily-recommend/daily-recommend.component';
import { DisplayRecomendationResultComponent } from './daily-recommend/display-recomendation-result/display-recomendation-result.component';
import { DisplaySelectedDishComponent } from './display-selected-dish/display-selected-dish.component';
import { RateDishComponent } from './rate-dish/rate-dish.component';

@NgModule({
  declarations: [
    AppComponent,
    FoodInformationComponent,
    FrontPageComponent,
    LoginComponent,
    RegisterComponent,
    RatingsComponent,
    DailyRecommendComponent,
    DisplayRecomendationResultComponent,
    DisplaySelectedDishComponent,
    RateDishComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule, 
    ReactiveFormsModule,
    HttpClientModule, 
    BrowserAnimationsModule, 
    MaterialModule,
    MatInputModule,
    MatButtonModule,
    MatListModule,
    MatStepperModule,
    NgbModule
  ],
  providers: [UserService],
  bootstrap: [AppComponent]
})
export class AppModule { }
