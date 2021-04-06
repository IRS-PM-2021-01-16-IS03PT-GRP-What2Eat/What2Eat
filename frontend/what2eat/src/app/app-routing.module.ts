import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FoodInformationComponent } from './components/food-information/food-information.component';    
import { FrontPageComponent } from './components/front-page/front-page.component'; 
import { LoginComponent } from './components/login/login.component'; 

const routes: Routes = [
  { path: '', redirectTo: '/frontpage', pathMatch: 'full' },
  { path: 'foodinformation/:id', component: FoodInformationComponent },
  { path: 'frontpage', component: FrontPageComponent },
  { path: 'login', component: LoginComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
