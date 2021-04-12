import {NgModule} from '@angular/core';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatIconModule} from '@angular/material/icon';
import {MatMenuModule} from '@angular/material/menu';

@NgModule({
    exports: [
        MatToolbarModule,
        MatIconModule,
        MatMenuModule,
    ]
  })
  
export class MaterialModule {}