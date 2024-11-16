from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

class AdminScreen(Screen):
    def __init__(self, **kwargs):
        super(AdminScreen, self).__init__(**kwargs)

        # Main layout (BoxLayout)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Set background color to white using canvas
        with self.canvas.before:
            Color(1, 1, 1, 1)  # White color (R, G, B, A)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self.update_rect, pos=self.update_rect)

        # Add Admin title at the top
        title = Button(text='Admin', font_size=24, size_hint=(1, None), height=50, background_normal='', background_color=(0, 0, 0, 0))
        layout.add_widget(title)

        # GridLayout to hold the data buttons
        grid_layout = GridLayout(cols=2, spacing=10, size_hint_y=None)
        grid_layout.bind(minimum_height=grid_layout.setter('height'))
        
        # Add buttons to the grid
        hotel_btn = Button(text='Data Hotel', size_hint_y=None, height=100)
        hotel_btn.bind(on_press=self.go_to_input)
        grid_layout.add_widget(hotel_btn)

        travel_btn = Button(text='Data Travel', size_hint_y=None, height=100)
        grid_layout.add_widget(travel_btn)

        kuliner_btn = Button(text='Data Kuliner', size_hint_y=None, height=100)
        grid_layout.add_widget(kuliner_btn)

        kereta_btn = Button(text='Data Kereta', size_hint_y=None, height=100)
        grid_layout.add_widget(kereta_btn)

        pesawat_btn = Button(text='Data Pesawat', size_hint_y=None, height=100)
        grid_layout.add_widget(pesawat_btn)

        layout.add_widget(grid_layout)

        self.add_widget(layout)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def go_to_input(self, instance):
        self.manager.current = 'input'
