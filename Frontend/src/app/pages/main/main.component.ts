import { Component, OnInit } from '@angular/core';
import { ImageService } from 'src/app/services/image.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit {
  text: string = "";
  constructor(private imageService: ImageService) { }

  ngOnInit(): void {
  }

  setText(text: string) {
    console.log(text);
    this.text = text;
  }

  createCloud() {
    this.imageService.generateCloud(this.text).subscribe(res => console.log(res));
    console.log('cloud')
  }

}
