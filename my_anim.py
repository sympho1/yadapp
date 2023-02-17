from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import Canvas, Line
from kivy.animation import Animation
from kivy.clock import Clock


class Testo(App):
    def build(self):
        self.layout = Widget()

        with self.layout.canvas:
            self.line = Line(points=(300, 100, 350, 100), width=10)
        
        Clock.schedule_interval(self.animate, 2)
        
        return self.layout

    def animate(self, dt):
        anim = Animation(points=(550, 100, 600, 100))
        anim += Animation(points=(300, 100, 350, 100))
        print(dt)

        anim.start(self.line)


if __name__ == "__main__":
    Testo().run()



