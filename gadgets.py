from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.behaviors import TouchRippleButtonBehavior, ButtonBehavior, ToggleButtonBehavior
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.metrics import dp, sp
from iconfonts import icon

from kivy.app import App

kv_gadgets = """
#: import icon iconfonts.icon
#: import CardTransition kivy.uix.screenmanager.CardTransition
#: import SwapTransition kivy.uix.screenmanager.SwapTransition
#: import FadeTransition kivy.uix.screenmanager.FadeTransition

<Bar>:
    _color: "000000"
    canvas:
        Color:
            hsv: 0, 0, .95
        Rectangle:
            pos: self.pos
            size: self.size[0], self.size[1]
        Color:
            hsv: 0, 0, .95
        Rectangle:
            pos: self.pos[0], self.pos[1] + sp(2)
            size: self.size[0], self.size[1]
    BoxLayout:
        size_hint_x: .05
    BoxLayout:
        padding: [dp(10), 0, 0, 0]
        size_hint_x: .3
        Label:
            markup: True            
            text: f"[b][color=000000]{root.left_corner}[/color][/b]"
            text_size: self.width + dp(50), None
            font_size: dp(22)                 
            
    BoxLayout:
        size_hint_x: .15
    BoxLayout:
        size_hint_x: .15
    BoxLayout:
        size_hint_x: .15
    ClickableBox:
        on_press:
            root.return_to_previous()
        size_hint_x: .2
        Label:
            markup: True
            text: icon(f"{root.right_corner}" , int(dp(20)), f"{root._color}")
        
    
<ClickableBox@ButtonBehavior+BoxLayout>:

<CustomLabel>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(10),] * 4

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
    canvas:
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
            size_hint_y: .15
            SoldShow:
                text: "[color=#EA2F06][b]AFFICHER LE SOLDE[/b][/color]"
        BoxLayout:
            size_hint_y: .05
        BoxLayout:
            size_hint_y: .25
            Label:
                markup: True
                text: "[color=#00000][b]Derniere transaction[/b][/color]"
                font_size: dp(18)
            Label:
                size_hint_x: .2
            Label:
                markup: True
                text: "[color=#EA2F06][b]VOIR PLUS   >[/b][/color]"
                font_size: dp(20)

        BoxLayout:
            size_hint_y: .55
            RelativeLayout:
                # center: self.parent.center
                size_hint_x: .15
                # padding: 15, 20
                RoundLabel:
                    # center: self.parent.center
                    size_hint: None, None
                    size: dp(40), dp(40)
                    pos_hint: {"center_x": .4, "center_y": .5}                    
            GridLayout:
                spacing: dp(5)
                padding: dp(20)
                cols: 3
                rows: 2
                size_hint_x: .85
                BoxLayout:
                    size_hint_x: .4
                    Label:
                        markup: True
                        size: dp(self.texture_size[0]), dp(self.texture_size[1])
                        #halign: "right"
                        text_size: dp(self.parent.size[0]) + dp(50), dp(self.size[1])
                        halign: "left"
                        text: "[color=#000000][b]2250748078646[/b][/color]"
                        font_size: dp(15)
                BoxLayout:
                    size_hint_x: .2
                BoxLayout:
                    size_hint_x: .4
                    Label:
                        markup: True
                        size: dp(self.texture_size[0]), dp(self.texture_size[1])
                        text_size: dp(self.size[0]), dp(self.size[1])
                        halign: "right"
                        text: "[color=#000000][b]- 1000 F CFA[/b][/color]"
                        font_size: dp(15)
                BoxLayout:
                    size_hint_x: .4
                    Label:
                        markup: True
                        size: dp(self.texture_size[0]), dp(self.texture_size[1])
                        text_size: dp(self.size[0]) + dp(50), dp(self.size[1])
                        halign: "left"
                        text: "[color=#000000][i]Paiement marchand[/i][/color]"
                        font_size: dp(15)
                BoxLayout:
                    size_hint_x: .2
                BoxLayout:
                    size_hint_x: .4
                    Label:                        
                        markup: True
                        size: dp(self.texture_size[0]), dp(self.texture_size[1])
                        text_size: dp(self.size[0]), dp(self.size[1]) #- dp(10) , None
                        halign: "right"
                        # id: trans
                        text: f"[color=#00000][i]22:50[/i][/color]"
                        font_size: dp(15)
                

<RoundLabel>:
    # size: dp(40), dp(40)
    canvas:
        Color:
            hsv: 0, .15, .15
            a: .5
        Ellipse:
            pos: self.pos
            size: self.size #dp(self.size[0]), dp(self.size[1])
    Label:
        center: root.center
        markup: True
        text: f'{icon("icon-shopping-basket", int(dp(18)), "ffffff")}'

<SoldShow>:
    canvas:
        Color:
            # hsv: 0, 0, .95
            rgba: 1, 1, 1, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(10),] * 4
    Label:
        id: text_id
        center: root.center
        markup: True
        text: root.text
        font_size: dp(18)
    Label:
        id: icony_id
        center: root.center[0] - dp(100), root.center[1]
        markup: True
        text: icon(f"{root.icony}", int(dp(18)), "#EA2F06")

<AstuceBox>:
    cols: 2
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: (dp(10), ) * 4
    BoxLayout:
        size_hint_x: .25
        canvas:
            # Color:
            #     rgba: .5, .25, .125, 1
            RoundedRectangle:
                pos: self.pos
                size: self.size
                source: root.src
                radius: dp(10), dp(0), dp(0), dp(10)
    BoxLayout:
        size_hint_x: .75
        GridLayout:
            rows: 3
            BoxLayout:
                size_hint_y: .45
                Label:
                    id: desc_text_id
                    size: dp(self.texture_size[0]), dp(self.texture_size[1])
                    text_size: self.parent.width - dp(25), None
                    font_size: dp(15)
                    # halign: "left"
                    text: f"[color=#000000]{root.description_text}[/color]"
                    markup: True
            BoxLayout:
                size_hint_y: .25
            BoxLayout:
                size_hint_y: .3
                ClickableLabel:
                    size: dp(self.texture_size[0]), dp(self.texture_size[1])
                    text_size: self.parent.width - dp(25), None
                    font_size: dp(22)
                    text: f"[color=#EA2F06][b][ref={root.click_text}]{root.click_text}[/ref][/b][/color]"
                    markup: True
                    on_ref_press: 
                        print(f"{desc_text_id.font_size}")
                        app.sm.transition = CardTransition()
                        app.sm.current = "sharepage"

<BarBottom>:
    canvas:
        Color:
            # rgba: .5, .25, .75, .3
            hsv: 0, 0, .95
        Rectangle:
            pos: self.pos
            size: self.size
    GridClickable:
        _text: "Acceuil"
        icony: "icon-home"
        on_press:
            app.sm.transition = FadeTransition()
            app.sm.current = "homepage"
    GridClickable:
        _text: "Nos partenaires"
        icony: "icon-exchange"
        on_press:
            app.sm.transition = FadeTransition()
            app.sm.current = "partnairpage"
    GridClickable:
        _text: "Mon compte"
        icony: "icon-user"
        on_press:
            app.sm.transition = FadeTransition()
            app.sm.current = "accountpage"

<GridClickable>:
    _text: ""
    # _icon: ""
    # _color: "000000"
    rows: 2
    padding: dp(3), dp(20), dp(3), dp(13)
    BoxLayout:
        Label:
            markup: True
            text: icon(f"{root.icony}" , int(dp(25)), f"{root._color}")
            id: icony_id
    BoxLayout:
        Label:
            text: root._text
            color: root._color
            font_size: "18sp"
            id: text_id

    


<Box>:
    padding: dp(20)

    Widget:
        canvas:
            Color:
                rgba: 1, 1, 1, 1
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [dp(10), ] * 4

            Color:
                rgba: 1, 1, 1, 1
            RoundedRectangle:
                pos: self.pos[0] + dp(5), self.pos[1]
                size: self.size[0] - dp(10), self.size[1] - dp(10)
                radius: [dp(10), ] * 4
                source: root.src

<Rondal>:
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Ellipse:
            pos: self.pos
            size: self.size

        Ellipse:
            pos: self.pos[0] + 5, self.pos[1] + 5
            #size: dp(self.size[0] - 10), dp(self.size[1] - 10)
            size: self.size[0] - 10, self.size[1] - 10
            source: root.src

    
"""

class Rondal(Widget):
    src = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.padding = 20, 20

class Box(BoxLayout):
    src = StringProperty("")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = None, None
        self.size = (dp(150),) * 2
    pass

class ClickableLabel(ButtonBehavior, Label):
    pass

class GridClickable(ToggleButtonBehavior, GridLayout):
    icony = StringProperty("icon-exchange")
    _color = "000000"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.group = "mygroup"

    def on_state(self, widget, value):
        if value == "down":
            self._color = "#EA2F06"
            self.ids.text_id.color = self._color
            self.ids.icony_id.text = icon(f"{self.icony}" , int(dp(25)), f"{self._color}")
            # print(self._color)
        else:
            self._color = "000000"
            self.ids.text_id.color = self._color
            self.ids.icony_id.text = icon(f"{self.icony}" , int(dp(25)), f"{self._color}")

class AstuceBox(GridLayout):
    src = StringProperty("")
    description_text = StringProperty("")
    click_text = StringProperty("")
    pass

class Bar(BoxLayout):
    left_corner = StringProperty("Acceuil")
    right_corner = StringProperty("icon-bell-alt")
    def __init__(self, **kwargs):
        # self.orientation = "vertical"
        super().__init__(**kwargs)

    def return_to_previous(self, *args):
        app = App.get_running_app()
        print(args)
        if self.right_corner != "icon-bell-alt":
            app.sm.current = "homepage"
            pass
        

class BarBottom(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pos_hint = {"y": 0}
        self.size_hint = 1, None
    pass


class CustomLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.size = self.texture_size
        # self.text_size = self.size[0], None
        self.valign = 'middle'
        self.halign = 'center'

        

class SoldBox(BoxLayout):
    trans = StringProperty()
  

class RoundLabel(Widget):
    pass


class SoldShow(ToggleButtonBehavior, Widget):
    icony = StringProperty("icon-eye-off")
    text = StringProperty("")
    
    def _change_text(self, icony, text):
        self.icony = icony
        self.text = text
        self.ids.icony_id.text = icon(f"{self.icony}", int(dp(18)), "#EA2F06")
        self.ids.text_id.color = "#EA2F06"
        self.ids.text_id.markup = True
        self.ids.text_id.font_size = dp(18)
        self.ids.text_id.bold = True
        self.ids.text_id.text = self.text
        pass

    def on_state(self, widget, value):
        if value == "down":
            self._change_text("icon-eye", "345000")
            print(widget.state)         
        else:
            self._change_text("icon-eye-off", "AFFICHER LE SOLDE")
            print(widget.state) 


Builder.load_string(kv_gadgets)
