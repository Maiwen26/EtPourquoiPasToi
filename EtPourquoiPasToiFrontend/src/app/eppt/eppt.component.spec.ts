import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EpptComponent } from './eppt.component';

describe('EpptComponent', () => {
  let component: EpptComponent;
  let fixture: ComponentFixture<EpptComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EpptComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EpptComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
