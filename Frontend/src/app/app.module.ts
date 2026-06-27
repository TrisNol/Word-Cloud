import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MainComponent } from './pages/main/main.component';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { FormsModule } from '@angular/forms';
import { DragAndDropComponent } from './components/drag-and-drop/drag-and-drop.component';
import { MatButtonModule } from '@angular/material/button';
import { provideHttpClient, withInterceptorsFromDi, withXhr } from '@angular/common/http';
import { DragDropModule } from '@angular/cdk/drag-drop';


@NgModule({
    declarations: [
        AppComponent,
        MainComponent,
        DragAndDropComponent
    ],
    bootstrap: [AppComponent], imports: [BrowserModule,
        AppRoutingModule,
        BrowserAnimationsModule,
        FormsModule,
        DragDropModule,
        MatFormFieldModule,
        MatInputModule,
        MatButtonModule], providers: [provideHttpClient(withXhr(), withInterceptorsFromDi())]
})
export class AppModule { }
