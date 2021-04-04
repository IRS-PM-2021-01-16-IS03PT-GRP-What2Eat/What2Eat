import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FoodInformationComponent } from './food-information/food-information.component';    // add this

const routes: Routes = [
  { path: '', redirectTo: '/foodinformation', pathMatch: 'full' },
  { path: 'foodinformation', component: FoodInformationComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
