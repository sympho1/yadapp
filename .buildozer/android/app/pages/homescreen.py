from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from gadgets import Bar

kv = """
#:import Bar gadgets.Bar
#:import CustomLabel gadgets.CustomLabel
#:import SoldBox gadgets.SoldBox

<HomePage>:
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

    CustomLabel:
        pos_hint: {"center_x": .225, "center_y": .9}
        size_hint: .4, None
        height: dp(25)

    SoldBox:
        pos_hint: {"center_x": .5, "center_y": .75}
        size_hint: .95, .25
        # height: dp(25)

"""


class HomePage(Screen):
    pass


Builder.load_string(kv)


