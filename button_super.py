from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import  Button
from kivy.app import App

class Controller1(FloatLayout):

    def __init__(self , **kwargs):
        super(Controller1, self).__init__(**kwargs)
        button = Button(text='Hello world' ,color={.9,.8,0,1}, font_size=15 , pos_hint={'x':.7, 'y':.8} , size_hint=(.1,.1))
        self.add_widget(button)
        button = Button(text='Hello world' ,color={.9,.9,0,1}, font_size=20 , pos_hint={'x':.5, 'y':.6} , size_hint=(.2,.2))
        self.add_widget(button)
        button = Button(text='Hello world' ,color={.9,1,0,1}, font_size=20 , pos_hint={'x':.2, 'y':.8} , size_hint=(.3,.4 ))
        self.add_widget(button)

class Controller2App(App):
    def build(self):
        return Controller1()

if __name__ == '__main__':
    Controller2App().run()