from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
import pyautogui
import time
from pynput.keyboard import Key, Controller
import pyperclip


class ChatSpammer(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10)

        self.title_label = Label(text="Chat Spammer", font_size=20)
        self.msg_label = Label(text="Enter message:")
        self.msg_entry = TextInput(multiline=False)
        self.times_label = Label(text="How many times:")
        self.times_entry = TextInput(multiline=False)
        self.start_button = Button(text="Start Spamming", on_press=self.start_spam)
        self.countdown_label = Label(text="", font_size=30)

        layout.add_widget(self.title_label)
        layout.add_widget(self.msg_label)
        layout.add_widget(self.msg_entry)
        layout.add_widget(self.times_label)
        layout.add_widget(self.times_entry)
        layout.add_widget(self.start_button)
        layout.add_widget(self.countdown_label)

        return layout

    def start_spam(self, instance):
        msg = self.msg_entry.text
        n = self.times_entry.text

        if msg and n.isdigit():
            count = 5
            self.countdown_label.text = str(count)
            Clock.schedule_interval(lambda dt: self.update_countdown(dt, msg, int(n)), 1)

    def update_countdown(self, dt, msg, n):
        count = self.countdown_label.text
        if count.isdigit():
            count = int(count)
            if count > 0:
                count -= 1
                self.countdown_label.text = str(count)
            else:
                self.countdown_label.text = "Spamming..."
                pyperclip.copy(msg)
                for i in range(n):
                    pyautogui.hotkey('ctrl', 'v')
                    pyautogui.press('enter')
                self.countdown_label.text = "Spamming Finish"


if __name__ == '__main__':
    ChatSpammer().run()
