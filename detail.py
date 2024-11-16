from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout

class RegionDetailScreen(Screen):
    def display_region_detail(self, img, text, description):
        # Mengatur gambar lokasi
        self.ids.detail_image.source = img
        
        # Mengatur nama lokasi
        self.ids.detail_text.text = text
        
        # Mengatur deskripsi lokasi
        self.ids.detail_description.text = description

    def go_back(self):
        self.manager.current = 'user'

    def on_trip_button_click(self):
        self.manager.current = 'travel_plan'
