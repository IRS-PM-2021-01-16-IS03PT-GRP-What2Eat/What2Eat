import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DisplaySelectedDishComponent } from './display-selected-dish.component';

describe('DisplaySelectedDishComponent', () => {
  let component: DisplaySelectedDishComponent;
  let fixture: ComponentFixture<DisplaySelectedDishComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DisplaySelectedDishComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DisplaySelectedDishComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
