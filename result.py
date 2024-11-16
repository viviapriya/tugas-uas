from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

class SearchResultScreen(Screen):
    def display_results(self, city_name):
        self.ids.city_label.text = city_name
        # Implement logic to display search results here
