from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import  Button
from kivy.app import App
from kivy.uix.label import  Label


class Controller2App(App):
    def build(self):
        return Label(text='[color=3333ff] Hello [/color] [color=ff3333] [b]World[/b][/color] ' , markup=True,
        font_size='60sp')

if __name__ == '__main__':
    Controller2App().run()