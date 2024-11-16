from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle

class UserScreen(Screen):
    def __init__(self, **kwargs):
        super(UserScreen, self).__init__(**kwargs)
        self.layout = None
        self.build_screen()

    def build_screen(self):
        # Set background canvas
        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self.update_rect, pos=self.update_rect)

        # Initialize main layout
        self.layout = BoxLayout(orientation='vertical')

        # Header layout
        header_layout = BoxLayout(orientation='horizontal', size_hint_y=0.2)
        header_layout.add_widget(Label(text="Happy\nHoliday", font_size=24, color=(1, 0.6, 0.6, 1)))
        header_layout.add_widget(Image(source='gambar/logo.jpg', size_hint_x=0.3, allow_stretch=True))
        self.layout.add_widget(header_layout)

        # Search layout
        search_layout = BoxLayout(orientation='horizontal', size_hint_y=0.1, padding=[10, 5])
        self.search_input = TextInput(hint_text="Masukkan nama kota...", size_hint_x=0.8, height=30)
        search_button = Button(text="Cari", size_hint_x=0.2)
        search_button.bind(on_press=self.search_city)
        search_layout.add_widget(self.search_input)
        search_layout.add_widget(search_button)
        self.layout.add_widget(search_layout)

        # Grid layout for places
        self.grid_layout = GridLayout(cols=3, spacing=10, padding=[10, 10], size_hint_y=0.7)
        self.layout.add_widget(self.grid_layout)
        self.add_widget(self.layout)

        # Populate places
        self.populate_places()

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def search_city(self, instance):
        city_name = self.search_input.text
        print(f"Mencari kota: {city_name}")
        # Switch to search_result screen
        self.manager.current = 'search_result'
        search_result_screen = self.manager.get_screen('search_result')
        search_result_screen.display_results(city_name)  # Display search results based on city name

    def populate_places(self):
        # Sample places list
        items = [
            ("gambar/umbul ponggok.jpg", "Umbul Ponggok", "Tempat wisata dengan air jernih untuk snorkeling."),
            ("gambar/soko langit.jpg", "Soko Langit", "Pemandangan pegunungan yang indah."),
            ("gambar/pusur tubing.jpg", "Pusur Tubing", "Pengalaman tubing seru di sungai."),
            ("gambar/kopi klotok.jpg", "Kopi Klotok", "Kedai kopi khas dengan suasana pedesaan."),
            ("gambar/selat solo.jpg", "Selat Solo", "Laut dengan hidangan seafood lezat."),
            ("gambar/soto triwindu.jpg", "Soto Triwindu", "Tempat makan terkenal dengan soto Solo."),
            ("gambar/hotel phoenix.jpg", "Hotel Phoenix", "Hotel berbintang dengan fasilitas mewah."),
            ("gambar/sunan hotel.jpg", "Sunan Hotel", "Akomodasi nyaman di pusat kota."),
            ("gambar/tjokro_hotel.jpg", "Tjokro Hotel", "Hotel berbintang dengan layanan terbaik."),
        ]

        for img, text, description in items:
            box = BoxLayout(orientation='vertical')
            image = Image(source=img, size_hint=(1, 0.8))
            image.bind(on_touch_down=lambda instance, touch, img=img, text=text, description=description: self.on_image_click(instance, touch, img, text, description))
            label = Label(text=text, font_size=12, size_hint=(1, 0.2))
            box.add_widget(image)
            box.add_widget(label)
            self.grid_layout.add_widget(box)

    def on_image_click(self, instance, touch, img, text, description):
        if instance.collide_point(*touch.pos):
            try:
                print(f"Menampilkan rincian untuk {text}")
                # Navigate to detail screen
                self.manager.current = 'region_detail'
                region_detail_screen = self.manager.get_screen('region_detail')
                region_detail_screen.display_region_detail(img, text, description)
            except Exception as e:
                print("Error saat mencoba menampilkan halaman detail:", e)
