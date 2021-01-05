from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string('''
BoxLayout:
    orientation: 'vertical'
    size_hint_y:None
    hight: sp(150)
    Label:
        text:'Hello'
    Button:
        text:'World'




'''))