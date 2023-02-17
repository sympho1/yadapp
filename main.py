from kivy.config import Config

Config.set("graphics", "width", 430)
Config.set("graphics", "height", 850)

import iconfonts
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager
from kivy.metrics import sp, dp
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.button import Button

from pages.homescreen import HomePage
from pages.sharescreen import SharePage
from pages.accountscreen import AccountPage
from pages.partnairscreen import PartnairPage

from gadgets import BarBottom


class MainWidget(FloatLayout):
    pass

class Yad(App):
    sm = ScreenManager()

    def build(self):
        self.home_page = HomePage(name="homepage")
        self.share_page = SharePage(name="sharepage")
        self.account_page = AccountPage(name="accountpage")
        self.partnair_page = PartnairPage(name="partnairpage")

        # self.marker = MapMarker(lat=5.37, lon=-3.90)
        # self.map = MapView(lat=5.37, lon=-3.90, zoom=11)
        # self.map.pos_hint = {"center_x": .5, "center_y": .5}
        # self.map.size_hint = [1, None]
        # self.map.height = Window.height - dp(100) 
        # self.map.add_marker(self.marker)
        # self.home_page.add_widget(self.map)

        # self.btn = Button(size_hint=[None, None], size=[200, 40])
        # self.btn.markup = True
        # self.btn.text = iconfonts.icon(f"icon-spin1", 32, "ffa33b")
        # self.home_page.add_widget(self.btn)
        self.sm.add_widget(self.home_page)
        self.sm.add_widget(self.share_page)
        self.sm.add_widget(self.account_page)
        self.sm.add_widget(self.partnair_page)

        self.main_widget = MainWidget()
        self.menu_bar = BarBottom()
        self.menu_bar.height = dp(80)
        
        self.main_widget.add_widget(self.sm)
        self.main_widget.add_widget(self.menu_bar)
        return self.main_widget


if __name__ == "__main__":
    iconfonts.register("fontello", "fontello.ttf", "fontello.fontd")
    Yad().run()
