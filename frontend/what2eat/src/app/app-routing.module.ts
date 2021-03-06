import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FrontPageComponent } from './components/front-page/front-page.component'; 
import { LoginComponent } from './components/login/login.component'; 
import { RegisterComponent } from './components/register/register.component';
import { DailyRecommendComponent } from './daily-recommend/daily-recommend.component';
import { DisplayRecomendationResultComponent } from './daily-recommend/display-recomendation-result/display-recomendation-result.component';
import { DisplaySelectedDishComponent } from './display-selected-dish/display-selected-dish.component';
import { RateDishComponent } from './rate-dish/rate-dish.component';

const routes: Routes = [
  { path: '', redirectTo: '/frontpage', pathMatch: 'full' },
  { path: 'frontpage', component: FrontPageComponent },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'howDoYouFeelToday', component: DailyRecommendComponent },
  { path: 'recommendationList', component: DisplayRecomendationResultComponent },
  { path: 'selectedDish', component: DisplaySelectedDishComponent},
  { path: 'rateADish', component: RateDishComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
