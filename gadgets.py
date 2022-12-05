from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.behaviors import TouchRippleButtonBehavior
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

kv_gadgets = """
#: import icon iconfonts.icon
<Bar>:
    canvas:
        Color:
            # rgba: 245/255, 242/255, 242/255, 1
            hsv: 0, 0, .95
        Rectangle:
            pos: self.pos
            size: self.size[0], self.size[1]
        Color:
            # rgba: 245/255, 242/255, 242/255, 1
            hsv: 0, 0, .95
        Rectangle:
            pos: self.pos[0], self.pos[1] + sp(2)
            size: self.size[0], self.size[1]
    BoxLayout:
        size_hint_x: .05
    BoxLayout:
        #padding: [40, 0, 0, 0]
        size_hint_x: .3
        Label:
            markup: True
            # text: "ACCEUIL" #f'{icon("icon-bell-alt", int(sp(32)), "000000")}'
            text: "[b][color=000000]Acceuil[/color][/b]"
            text_size: self.width, None
            font_size: dp(25) # '25dp'
            
            
            
    BoxLayout:
        size_hint_x: .15
    BoxLayout:
        size_hint_x: .15
    BoxLayout:
        size_hint_x: .15
    BoxLayout:
        size_hint_x: .2
        Label:
            markup: True
            text: f'{icon("icon-bell-alt", int(dp(20)), "000000")}'
    

<CustomLabel>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [10,] * 4

    markup: True
    text: "[color=000000][b]Compte Principal[/b][/color]"
    text_size: root.width, None
    font_size: dp(18) #'20sp'
    # valign: 'middle'
    # halign: 'center'
    padding: 10, 10

<SoldBox>:
    # orientation: "vertical"
    # trans: trans
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(10),] * 4
    BoxLayout:
        center: root.center
        orientation: "vertical"
        BoxLayout:
            size_hint_y: .3
            Label:
                markup: True
                text: "[color=#FFA500][b]Afficher le Solde[/b][/color]"
                font_size: dp(20) #'20sp'
        BoxLayout:
            size_hint_y: .1
        BoxLayout:
            size_hint_y: .2
            Label:
                markup: True
                text: "[color=#00000][b]Derniere transaction[/b][/color]"
                font_size: dp(18)
            Label:
                size_hint_x: .2
            Label:
                markup: True
                text: "[color=#FFA500][b]VOIR PLUS[/b][/color]"
                font_size: dp(20)

        BoxLayout:
            size_hint_y: .4
            Widget:
                center: self.parent.center
                size_hint_x: .2
                # padding: 15, 20
                RoundLabel:
                    center: self.parent.center
                    size: dp(40), dp(40)
                    
            GridLayout:
                padding: 20
                cols: 3
                rows: 2
                BoxLayout:
                    Label:
                        markup: True
                        text: "[color=#000000][b]2250748078646[/b][/color]"
                        font_size: dp(15)
                BoxLayout:
                BoxLayout:
                    Label:
                        markup: True
                        text: "[color=#000000][b]- 1000 F CFA[/b][/color]"
                        font_size: dp(15)
                BoxLayout:
                    Label:
                        markup: True
                        text: "[color=#000000][i]Paiement marchand[/i][/color]"
                        font_size: dp(15)
                BoxLayout:
                BoxLayout:
                    Label:
                        markup: True
                        # id: trans
                        text: f"[color=#00000][i]{root.trans}[/i][/color]"
                        font_size: dp(15)
                

<RoundLabel>:
    size: 40, 40
    canvas.before:
        Color:
            hsv: 0, .15, .75
        Ellipse:
            pos: self.pos
            size: dp(self.size[0]), dp(self.size[1])
    Label:
        center: root.center
        markup: True
        text: f'{icon("icon-shopping-basket", int(dp(18)), "ffffff")}'

    
"""

class Bar(BoxLayout):
    def __init__(self, **kwargs):
        # self.orientation = "vertical"
        super().__init__(**kwargs)
    pass

class CustomLabel(Label):
    def __init__(self, **kwargs):
        self.size = self.texture_size
        # self.text_size = self.size[0], None
        self.valign = 'middle'
        self.halign = 'center'

        super().__init__(**kwargs)

    
    pass


class SoldBox(TouchRippleButtonBehavior, BoxLayout):
    # def on_press(self, **kwargs):
    #     print()
    #     return super().on_press(**kwargs)
    
    trans = StringProperty()
    def on_touch_down(self, touch):
        collide_point = self.collide_point(touch.x, touch.y)
        if collide_point:
            touch.grab(self)
            self.ripple_show(touch)
            return True
        return False

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            self.ripple_fade()
            return True
        return False

class RoundLabel(Widget):
    pass

Builder.load_string(kv_gadgets)