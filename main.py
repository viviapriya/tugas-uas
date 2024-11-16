from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from login import LoginScreen
from admin import AdminScreen
from user import UserScreen
from result import SearchResultScreen
from detail import RegionDetailScreen
from plan import TravelPlanScreen
from schedule import ScheduleScreen
from kivy.core.window import Window

class MyApp(App):
    def build(self):

        Window.size = (360, 640)

        Builder.load_file('login.kv')
        Builder.load_file('admin.kv')
        Builder.load_file('user.kv')
        Builder.load_file('result.kv')
        Builder.load_file('detail.kv')
        Builder.load_file('plan.kv')
        Builder.load_file('schedule.kv')

        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(AdminScreen(name='admin'))
        sm.add_widget(UserScreen(name='user'))
        sm.add_widget(SearchResultScreen(name='search_result'))
        sm.add_widget(RegionDetailScreen(name='region_detail'))
        sm.add_widget(TravelPlanScreen(name='travel_plan'))
        sm.add_widget(ScheduleScreen(name='schedule'))

        return sm

if __name__ == '__main__':
    MyApp().run()
