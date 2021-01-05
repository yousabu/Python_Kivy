from kivy.lang import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string('''

RelativeLayout:
    Button:
        text:'B1'
        size_hint: .4,.4
        pos: 50 , 100
    Button:
        text:'B2'
        size_hint: .3 , .3 
        pos_hint: {'x':.4 , 'y':.5 }



'''))