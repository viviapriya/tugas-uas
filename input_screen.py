from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

class InputScreen(Screen):
    def __init__(self, **kwargs):
        super(InputScreen, self).__init__(**kwargs)

        # Main layout (BoxLayout)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Set background color to white using canvas
        with self.canvas.before:
            Color(1, 1, 1, 1)  # White background
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self.update_rect, pos=self.update_rect)

        # Add input fields
        self.city = TextInput(hint_text="Kota", size_hint=(1, None), height=50)
        layout.add_widget(self.city)

        self.tour_name = TextInput(hint_text="Nama Wisata", size_hint=(1, None), height=50)
        layout.add_widget(self.tour_name)

        self.email = TextInput(hint_text="Email", size_hint=(1, None), height=50)
        layout.add_widget(self.email)

        self.location = TextInput(hint_text="Lokasi", size_hint=(1, None), height=50)
        layout.add_widget(self.location)

        # Add buttons
        submit_button = Button(text="Submit", size_hint=(1, None), height=50)
        submit_button.bind(on_press=self.submit_data)
        layout.add_widget(submit_button)

        back_button = Button(text="Kembali", size_hint=(1, None), height=50)
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def submit_data(self, instance):
        color=(0, 0, 0, 1)
        # You can handle the data submission logic here
        self.manager.current = 'result'

    def go_back(self, instance):
        self.manager.current = 'admin'
