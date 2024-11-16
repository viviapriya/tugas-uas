from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.username = None
        self.password = None

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def check_login(self, instance):
        if self.username.text == "admin" and self.password.text == "adminpass":
            self.manager.current = 'admin'
        elif self.username.text == "ti22a1" and self.password.text == "123456":
            self.manager.current = 'user'
        else:
            print("Username atau password salah")
