import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DisplayRecomendationResultComponent } from './display-recomendation-result.component';

describe('DisplayRecomendationResultComponent', () => {
  let component: DisplayRecomendationResultComponent;
  let fixture: ComponentFixture<DisplayRecomendationResultComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DisplayRecomendationResultComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DisplayRecomendationResultComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
