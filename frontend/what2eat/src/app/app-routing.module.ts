import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FoodInformationComponent } from './components/food-information/food-information.component';    
import { FrontPageComponent } from './components/front-page/front-page.component'; 
import { LoginComponent } from './components/login/login.component'; 
import { RegisterComponent } from './components/register/register.component';
import { RatingsComponent } from './components/ratings/ratings.component';
import { DailyRecommendComponent } from './daily-recommend/daily-recommend.component';

const routes: Routes = [
  { path: '', redirectTo: '/frontpage', pathMatch: 'full' },
  { path: 'ratings', component: RatingsComponent },
  { path: 'foodinformation', component: FoodInformationComponent },
  { path: 'frontpage', component: FrontPageComponent },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'howDoYouFeelToday', component: DailyRecommendComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
