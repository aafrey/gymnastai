from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from anthropometry import Anthropometry
from dailylog import DailyLog
from liftinginfo import LiftingInfo


Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')

Builder.load_file('dailylog.kv')
Builder.load_file('anthropometry.kv')
Builder.load_file('liftinginfo.kv')
Builder.load_file('landingpage.kv')

from kivy.garden.navigationdrawer import NavigationDrawer


class Gymnastai(NavigationDrawer):

    def add_measurements_page(self):
        self.ids._main_container.clear_widgets()
        self.ids._main_container.add_widget(Anthropometry())

    def add_daily_log_page(self):
        self.ids._main_container.clear_widgets()
        self.ids._main_container.add_widget(DailyLog())

    def add_pr_page(self):
        self.ids._main_container.clear_widgets()
        self.ids._main_container.add_widget(LiftingInfo())

    def toggle_state(self, animate=True):
        '''Toggles from open to closed or vice versa, optionally animating or
        simply jumping.'''
        if self.state == 'open':
            if animate:
                self.anim_to_state('closed')
            else:
                self.state = 'closed'
        elif self.state == 'closed':
            if animate:
                self.anim_to_state('open')
            else:
                self.state = 'open'


class GymnastaiApp(App):
    pass

if __name__ == '__main__':
    GymnastaiApp().run()