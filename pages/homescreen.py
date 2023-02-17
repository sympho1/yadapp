from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from gadgets import Bar

kv = """
#:import Bar gadgets.Bar
#:import Box gadgets.Box
#:import Rondal gadgets.Rondal
#:import BarBottom gadgets.BarBottom
#:import CustomLabel gadgets.CustomLabel
#:import SoldBox gadgets.SoldBox
#:import AstuceBox gadgets.AstuceBox
#:import Window kivy.core.window.Window

<HomePage>:
    canvas:
        Color:
            # rgba: 245/255, 242/255, 242/255, 1
            hsv: 0, 0, .95
            a: 1
        Rectangle:
            pos: self.pos
            size: self.size

    ScrollView:
        do_scroll_x: False
        do_scroll_y: True
        size_hint: 1, None
        height: Window.height - bar_id.height
        pos_hint: {"y": barbottom_id.height / Window.height}        

        BoxLayout:
            size_hint_y: None
            height: self.parent.height * 1.8          
            
            orientation: "vertical"
            spacing: dp(10)
            padding: dp(10), 0
            BoxLayout:
                size_hint_y: .01

            RelativeLayout:
                size_hint_y: .1
                CustomLabel:
                    size_hint: .4, None
                    height: dp(38)

            RelativeLayout:                
                size_hint_y: .17
                SoldBox:                    
                    # height: dp(25)

            
            RelativeLayout:
                size_hint_y: .3
                
                Label:
                    pos_hint: {"x": 0.025, "center_y": .72}
                    size: dp(self.texture_size[0]), dp(self.texture_size[1])
                    text_size: self.parent.width, dp(30)
                    markup: True
                    halign: "left"
                    text: "[b]Mes services[/b]"
                    color: "#000000"
                    font_size: dp(20)
                Box:
                    id: box_id
                    src: "imgs/4159.jpg" 
                    pos_hint: {"center_x": .15, "center_y": .5}  
                Label:
                    pos_hint: {"center_x": .15, "center_y": .28}
                    size: dp(self.texture_size[0]), dp(self.texture_size[1])
                    text_size: box_id.width/1.5 , None
                    text: "[b]Recharger du crédit[/b]"
                    markup: True
                    halign: "center"
                    color: "#000000"            
                Box:
                    src: "imgs/4143.jpg"
                    pos_hint: {"center_x": .5, "center_y": .5}
                Label:
                    pos_hint: {"center_x": .5, "center_y": .28}
                    size: dp(self.texture_size[0]), dp(self.texture_size[1])
                    text_size: box_id.width/1.5 , None
                    text: "[b]Transferer de l'argent[/b]"
                    markup: True
                    halign: "center"
                    color: "#000000"
                Box:
                    src: "imgs/2158.jpg"  
                    pos_hint: {"center_x": .85, "center_y": .5}
                Label:
                    pos_hint: {"center_x": .85, "center_y": .28}
                    size: dp(self.texture_size[0]), dp(self.texture_size[1])
                    text_size: box_id.width/1.5 , None
                    text: "[b]Acheter un Pass[/b]"
                    markup: True
                    halign: "center"
                    color: "#000000"
            ScrollView:                    
                do_scroll_x: True 
                do_scroll_y: False
                size_hint: None, .08 # 1
                width: dp(self.parent.width)
                bar_color: 1, 1, 1, 0
                bar_inactive_color: 1, 1, 1, 0

                GridLayout:
                    size_hint_x: None
                    width: dp(root.width) * (1 + 1/8)
                    rows: 1
                    #RelativeLayout:
                    padding: dp(5)
                    spacing: dp(20)
                    Rondal:
                        size_hint: None, None                          
                        size: dp(70), dp(70)
                        src: "imgs/2158.jpg"
                        #pos_hint: {"center_x": .25, "center_y": .5}
                    #RelativeLayout:
                    Rondal:
                        size_hint: None, None                          
                        size: dp(70), dp(70)
                        src: "imgs/4143.jpg"
                        #pos_hint: {"center_x": .25, "center_y": .5}
                    #RelativeLayout:
                    Rondal:
                        size_hint: None, None                          
                        size: dp(70), dp(70)
                        src: "imgs/4159.jpg"
                        #pos_hint: {"center_x": .25, "center_y": .5}
                    #RelativeLayout:
                    Rondal:
                        size_hint: None, None                          
                        size: dp(70), dp(70)
                        src: "imgs/2158.jpg"
                        #pos_hint: {"center_x": .25, "center_y": .5}
                    #RelativeLayout:
                    Rondal:
                        size_hint: None, None                          
                        size: dp(70), dp(70)
                        src: "imgs/4143.jpg"
                        #pos_hint: {"center_x": .25, "center_y": .5}
                    # #RelativeLayout:
                    # Rondal:
                    #     size_hint: 1, 1                            
                    #     size: 30, 30
                    #     src: "imgs/4159.jpg"
                    #     #pos_hint: {"center_x": .25, "center_y": .5}


            RelativeLayout:
                size_hint_y: .03
                Label:
                    size: dp(self.texture_size[0]), dp(self.texture_size[1])
                    text_size: self.parent.width, dp(30)
                    markup: True
                    halign: "left"
                    text: "[b]Astuces[/b]"
                    color: "#000000"
                    font_size: dp(20)
            BoxLayout:
                size_hint_y: .3
                orientation: "vertical"
                spacing: dp(10)
                BoxLayout:
                    
                    #size_hint: 1, None
                    #size: .8, dp(110)
                    AstuceBox:
                        src: "imgs/1985.jpg"
                        #pos_hint: {"center_x": .5, "center_y": .5}
                        description_text: "Partager l'application Yadapp avec vos proches"
                        click_text: "Partager"

                BoxLayout:
                    
                    #size_hint: 1, None
                    #size: .8, dp(110)
                    AstuceBox:
                        src: "imgs/4159.jpg"                        
                        
                        description_text: "Scanner un QR code en lien avec un service Orange Money"
                        click_text: "Scanner"

                BoxLayout:
                    
                    #size_hint: 1, None
                    #size: .8, dp(110)
                    AstuceBox:
                        src: "imgs/2158.jpg"                        
                        
                        description_text: "Liberez votre esprit en programmant vos transferts automatiques"
                        click_text: "Transferer"
                BoxLayout:
                    
                    # size_hint: 1, None
                    # size: .8, dp(110)
                    AstuceBox:
                        src: "imgs/2158.jpg"                       
                        
                        description_text: "Liberez votre esprit en programmant vos transferts automatiques"
                        click_text: "Transferer"

            BoxLayout:
                size_hint_y: .01
    Bar:
        id: bar_id
        pos_hint: {"top": 1}
        size_hint: 1, None
        height: dp(51)
    FloatLayout:            
        id: barbottom_id
        pos_hint: {"y": 0}
        size_hint: 1, None
        height: dp(80)
"""


class HomePage(Screen):
    pass


Builder.load_string(kv)


