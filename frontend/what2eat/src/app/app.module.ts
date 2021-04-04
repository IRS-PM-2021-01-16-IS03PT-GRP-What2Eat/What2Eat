import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { HttpClientModule } from '@angular/common/http';    // add this
import { FormsModule } from '@angular/forms';    // add this
import { UserService } from './user.service';
import { FoodInformationComponent } from './food-information/food-information.component';    // add this

@NgModule({
  declarations: [
    AppComponent,
    FoodInformationComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule, 
    HttpClientModule,
  ],
  providers: [UserService],
  bootstrap: [AppComponent]
})
export class AppModule { }
