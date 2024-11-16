from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

class AdminScreen(Screen):
    def logout(self, instance):
        self.manager.current = 'login'
