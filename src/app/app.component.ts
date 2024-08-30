// src/app/app.component.ts
import { Component } from '@angular/core';
import { ChatService } from './chat.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Groq Chat App';
  message: string = '';
  chatHistory: { text: string, sender: string }[] = [];

  constructor(private chatService: ChatService) { }

  sendMessage(): void {
    if (this.message.trim()) {
      this.chatHistory.push({ text: this.message, sender: 'user' });
      this.chatService.sendMessage(this.message).subscribe(
        res => {
          this.chatHistory.push({ text: res.reply, sender: 'bot' });
          this.message = ''; // Clear the input field after sending the message
        },
        err => {
          console.error(err);
          this.chatHistory.push({ text: 'An error occurred while sending the message.', sender: 'bot' });
        }
      );
    }
  }

  clearChat(): void {
    this.chatHistory = [];
  }
}
