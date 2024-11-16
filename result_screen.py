from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)

        # Main layout (BoxLayout)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Set background color to white using canvas
        with self.canvas.before:
            Color(1, 1, 1, 1)  # White background
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self.update_rect, pos=self.update_rect)

        # Display result with custom text color
        self.result_label = Label(text="Hasil Inputan Anda", font_size=18, color=(0, 0, 0, 1))  # Black text
        layout.add_widget(self.result_label)

        # Add a button to go back with custom text color
        back_button = Button(text="Kembali ke Admin", size_hint=(1, None), height=50, color=(1, 1, 1, 1))  # white text
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def go_back(self, instance):
        self.manager.current = 'admin'
