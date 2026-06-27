import { CdkDragDrop, moveItemInArray } from '@angular/cdk/drag-drop';
import { ChangeDetectionStrategy, Component, EventEmitter, Output } from '@angular/core';

@Component({
    selector: 'app-drag-and-drop',
    templateUrl: './drag-and-drop.component.html',
    styleUrls: ['./drag-and-drop.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush,
    standalone: false
})
  export class DragAndDropComponent {
  files: File[] = [];
  isDraggingFile = false;

  @Output() textRead: EventEmitter<string> = new EventEmitter();
  @Output() imageRead: EventEmitter<string> = new EventEmitter();
  constructor() {}

  /**
 * format bytes
 * @param bytes (File size in bytes)
 * @param decimals (Decimals point)
 */
  formatBytes(bytes: number, decimals: number): string {
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

  drop(event: CdkDragDrop<File[]>) {
    moveItemInArray(this.files, event.previousIndex, event.currentIndex);
  }

  onDragOver(event: DragEvent) {
    event.preventDefault();
    this.isDraggingFile = true;
  }

  onDragLeave(event: DragEvent) {
    event.preventDefault();
    this.isDraggingFile = false;
  }

  onNativeDrop(event: DragEvent) {
    event.preventDefault();
    this.isDraggingFile = false;
    const droppedFiles = event.dataTransfer?.files;
    if (!droppedFiles) {
      return;
    }
    this.processFiles(droppedFiles);
  }

  fileBrowseHandler(files: FileList | null) {
    if (!files) {
      return;
    }
    this.processFiles(files);
  }

  private processFiles(files: FileList) {
    for (let i = 0; i < files.length; i++) {
      const file = files.item(i);
      if (!file) {
        continue;
      }

      this.files.push(file);
      const fileName = file.name.toLowerCase();

      if (fileName.endsWith('.txt')) {
        this.readTextFile(file);
      } else if (fileName.endsWith('.png') || fileName.endsWith('.jpg') || fileName.endsWith('.jpeg')) {
        this.readImageFile(file);
      }
    }
  }

  private readTextFile(file: File) {
    const reader = new FileReader();
    reader.onload = () => this.textRead.emit(String(reader.result ?? ''));
    reader.readAsText(file);
  }

  private readImageFile(file: File) {
    const reader = new FileReader();
    reader.onload = () => {
      const result = reader.result;
      if (typeof result === 'string') {
        this.imageRead.emit(result);
      }
    };
    reader.readAsDataURL(file);
  }
}
