from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

class TravelPlanScreen(Screen):
    def set_region_details(self, region_name, region_description):
        self.ids.selected_region.text = f"Perjalanan ke: {region_name}\nDeskripsi: {region_description}"

    def save_travel_plan(self):
        # Ambil data dari form
        region = self.ids.selected_region.text
        date = self.ids.date_input.text
        time = self.ids.time_input.text
        price = self.ids.price_input.text

        # Cek apakah data sudah benar
        print(f"Data yang disimpan: {region}, {date}, {time}, {price}")

        # Pindah ke halaman schedule dan tampilkan data
        schedule_screen = self.manager.get_screen('schedule')
        schedule_screen.display_schedule(region, date, time, price)
        self.manager.current = 'schedule'

    def go_back(self, instance):
        self.manager.current = 'region_detail'

    def save_travel_plan(self):
    # Proses simpan data perencanaan perjalanan
        self.manager.current = 'schedule'

