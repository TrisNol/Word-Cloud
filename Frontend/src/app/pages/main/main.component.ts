import { Component, OnInit } from '@angular/core';
import { ImageService } from 'src/app/services/image.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit {
  text: string = "";
  cloudImage: any;
  mask: any;
  width: number;
  height: number;
  constructor(private imageService: ImageService) { }

  ngOnInit(): void {
  }

  setText(text: string) {
    this.text = text;
  }
  setImage(image: any) {
    this.mask = image;
  }

  createCloud() {
    this.imageService.generateCloud(this.text).subscribe(res => {
      this.cloudImage = this.imageService.decodeImage(res.cloud);
      this.width = res.width;
      this.height = res.height;
    });
  }
  createMask() {
    this.imageService.generateMask(this.text, this.mask).subscribe(res => {
      this.cloudImage = this.imageService.decodeImage(res.cloud);
      this.width = res.width;
      this.height = res.height;
    });
  }

}
