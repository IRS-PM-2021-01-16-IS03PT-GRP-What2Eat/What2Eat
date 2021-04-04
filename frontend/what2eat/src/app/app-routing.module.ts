import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FoodInformationComponent } from './food-information/food-information.component';    
import { FrontPageComponent } from './front-page/front-page.component'; 
import { LoginComponent } from './login/login.component'; 

const routes: Routes = [
  { path: '', redirectTo: '/frontpage', pathMatch: 'full' },
  { path: 'foodinformation', component: FoodInformationComponent },
  { path: 'frontpage', component: FrontPageComponent },
  { path: 'login', component: LoginComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
