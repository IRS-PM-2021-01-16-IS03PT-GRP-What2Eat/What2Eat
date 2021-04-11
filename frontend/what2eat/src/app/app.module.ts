import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { HttpClientModule } from '@angular/common/http';  
import { FormsModule } from '@angular/forms';   
import { UserService } from './services/user.service';
import { FoodInformationComponent } from './components/food-information/food-information.component';
import { FrontPageComponent } from './components/front-page/front-page.component';
import { LoginComponent } from './components/login/login.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';  
import { MaterialModule } from './materials/material-module';
import { RegisterComponent } from './components/register/register.component';
import { RatingsComponent } from './components/ratings/ratings.component';

@NgModule({
  declarations: [
    AppComponent,
    FoodInformationComponent,
    FrontPageComponent,
    LoginComponent,
    RegisterComponent,
    RatingsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule, 
    HttpClientModule, 
    BrowserAnimationsModule, 
    MaterialModule
  ],
  providers: [UserService],
  bootstrap: [AppComponent]
})
export class AppModule { }
