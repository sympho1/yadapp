from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from gadgets import Bar

kv = """
#:import Bar gadgets.Bar
#:import CustomLabel gadgets.CustomLabel
#:import SoldBox gadgets.SoldBox
#:import AstuceBox gadgets.AstuceBox

<PartnairPage>:
    canvas:
        Color:
            # rgba: 245/255, 242/255, 242/255, 1
            hsv: 0, 0, .95
            a: 1
        Rectangle:
            pos: self.pos
            size: self.size

    Bar:
        id: bar_homepage
        pos_hint: {"top": 1}
        size_hint: 1, None
        height: dp(50)
        left_corner: "Nos Partenaires"
        right_corner: "icon-left-big"

"""


class PartnairPage(Screen):
    pass


Builder.load_string(kv)


