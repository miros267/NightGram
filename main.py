from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from telethon.sync import TelegramClient
import threading

API_ID = 37373231
API_HASH = 'f8a4c00a7dde341222da134cbb9ba6a0'
PHONE = '+79197641413'

class TelegramApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.status_label = Label(text='Нажмите кнопку для подключения', size_hint=(1, 0.2))
        self.connect_button = Button(text='Подключиться к Telegram', size_hint=(1, 0.2))
        self.connect_button.bind(on_press=self.connect_telegram)

        self.layout.add_widget(self.status_label)
        self.layout.add_widget(self.connect_button)
        return self.layout

    def connect_telegram(self, instance):
        self.status_label.text = 'Подключение...'
        thread = threading.Thread(target=self.run_client)
        thread.start()

    def run_client(self):
        client = TelegramClient('session_name', API_ID, API_HASH)
        client.start(phone=PHONE)
        me = client.get_me()
        self.status_label.text = f'Вошли как: {me.first_name}'
        client.disconnect()

if __name__ == '__main__':
    TelegramApp().run()
