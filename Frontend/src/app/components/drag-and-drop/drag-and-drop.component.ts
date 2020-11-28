import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-drag-and-drop',
  templateUrl: './drag-and-drop.component.html',
  styleUrls: ['./drag-and-drop.component.scss']
})
export class DragAndDropComponent implements OnInit {
  files: any[] = [];
  reader = new FileReader();

  @Output() textRead: EventEmitter<string> = new EventEmitter();
  constructor() {
    this.reader.onload = () => {
      let text = this.reader.result;
      this.textRead.emit(String(text));
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
      this.reader.readAsText(item);
    }
  }
  fileBrowseHandler(files: FileList) {
    for (let i = 0; i < files.length; i++) {
      this.files.push(files.item(i));
      this.reader.readAsText(files.item(i));
    }
  }
}
