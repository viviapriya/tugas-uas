from kivy.uix.screenmanager import Screen

class ScheduleScreen(Screen):
    def go_back(self):
        self.manager.current = 'user'  # Sesuaikan dengan layar sebelumnya
