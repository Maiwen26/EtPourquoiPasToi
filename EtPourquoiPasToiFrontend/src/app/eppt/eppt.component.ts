import { Component,OnInit } from '@angular/core';
//@Input() eppt!: eppt ; Pour qu'une propriété puisse être injectée depuis l'extérieur d'un component
@Component({
  selector: 'app-eppt',
  templateUrl: './eppt.component.html',
  styleUrls: ['./eppt.component.scss']
})
export class EpptComponent implements OnInit {
  title!: string;
  description! : string;
  createDate! : Date;
  snaps!:number;
  imageUrl!:string;
  buttonText!: string;

  ngOnInit()
  {
    this.title='Titre 1';
    this.description='Description 1';
    this.createDate=new Date();
    this.snaps=3;
    this.imageUrl = 'https://cdn.pixabay.com/photo/2015/05/31/16/03/teddy-bear-792273_1280.jpg';
    this.buttonText = 'Oh Snap!';
  }

   //Le nom de méthode qui commence par on signale que cette méthode répond à un événement.
  onSnap() {
    if (this.buttonText === 'Oh Snap!') {
      this.snaps++;
      this.buttonText = 'Oops, unSnap!';
    } else {
      this.snaps--;
      this.buttonText = 'Oh Snap!';
      }
    }

}


