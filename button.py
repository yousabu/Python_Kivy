from kivy.lang import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string('''
Label:
    Button:
        text:'Youssef'
        font_size : 32
        color: .8,.9,0,1
        size:200,100
        pos: 50,100
    Button:
        text:'Youssef'
        font_size : 25
        color: .8,.1,0,1
        size:200,100
        pos: 150,200

'''))