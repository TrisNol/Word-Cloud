import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ImageService {

  constructor(private http: HttpClient) { }

  public decodeImage(image){
    return 'data:image/jpg;base64,' + image; 
  }

  public generateCloud(text: string): Observable<any> {
    return this.http.post(environment.basehref + "/cloud", { text: text });
  }
  public generateMask(text: string, image: any): Observable<any> {
    return this.http.post(environment.basehref + "/mask", { text: text, image: image });
  }
}
