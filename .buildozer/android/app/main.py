from kivy.config import Config
Config.set("graphics", "width", 430)
Config.set("graphics", "height", 850)

import iconfonts
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager
from kivy.metrics import sp, dp 
# from kivy_garden.mapview import MapView, MapMarker
from kivy.core.window import Window
from kivy.uix.button import Button

from pages.homescreen import HomePage



class Yad(App):
    sm = ScreenManager()
    def build(self):
        self.home_page = HomePage(name="home_page")
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
        return self.sm


if __name__ == "__main__":
    iconfonts.register("fontello", "fontello.ttf", "fontello.fontd")
    Yad().run()