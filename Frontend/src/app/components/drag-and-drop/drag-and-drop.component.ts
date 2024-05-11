import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-drag-and-drop',
  templateUrl: './drag-and-drop.component.html',
  styleUrls: ['./drag-and-drop.component.scss']
})
export class DragAndDropComponent implements OnInit {
  files: any[] = [];
  textReader = new FileReader();
  imageReader = new FileReader();

  @Output() textRead: EventEmitter<string> = new EventEmitter();
  @Output() imageRead: EventEmitter<any> = new EventEmitter();
  constructor() {
    this.textReader.onload = () => {
      let text = this.textReader.result;
      this.textRead.emit(String(text));
    };
    this.imageReader.onload = () => {
      let image = this.imageReader.result;
      this.imageRead.emit(image);
    };
  }

  /**
 * format bytes
 * @param bytes (File size in bytes)
 * @param decimals (Decimals point)
 */
  formatBytes(bytes, decimals) {
    if (bytes === 0) {
      return '0 Bytes';
    }
    const k = 1024;
    const dm = decimals <= 0 ? 0 : decimals || 2;
    const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
  }

  /**
 * Delete file from files list
 * @param index (File index)
 */
  deleteFile(index: number) {
    this.files.splice(index, 1);
  }

  ngOnInit(): void {
  }

  onFileDropped($event) {
    for (const item of $event) {
      this.files.push(item);
      if(item.name.endsWith('.txt')){
        this.textReader.readAsText(item);
      }
      else if(item.name.endsWith('.png') || item.name.endsWith('.jpg')){
        this.imageReader.readAsDataURL(item);
      }
    }
  }
  fileBrowseHandler(files: FileList) {
    for (let i = 0; i < files.length; i++) {
      let file = files.item(i);
      this.files.push(file);
      if(file.name.endsWith('.txt')){
        this.textReader.readAsText(files.item(i));
      }
      else if(file.name.endsWith('.png') || file.name.endsWith('.jpg')){
        this.imageReader.readAsDataURL(file);
      }
    }
  }
}
