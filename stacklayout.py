from kivy.lang import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string('''

StackLayout:
    orintation: 'rl-tb'
    padding: 20
    spacing: 10
    Button:
        text:'B1'
        size_hint: .2 , .1
    Button:
        text:'B1'
        size_hint: .2 , .1
    Button:
        text:'B1'
        size_hint: .2 , .1
    Button:
        text:'B1'
        size_hint: .2 , .1



'''))