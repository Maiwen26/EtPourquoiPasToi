import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RechercheTemoignagesComponent } from './recherche-temoignages.component';

describe('RechercheTemoignagesComponent', () => {
  let component: RechercheTemoignagesComponent;
  let fixture: ComponentFixture<RechercheTemoignagesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RechercheTemoignagesComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RechercheTemoignagesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
