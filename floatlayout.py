from kivy.lang import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string("""
<Button>:
    color: .8,.2,0,1
    font_size: 50
    size_hint: 3, .2
FloatLayout:
    Button:
        text:'B1'
        pos_hint: {'x':0,'top': 1}     
    Button:
        text:'B1'
        pos_hint: {'y':0,'right': 1}


"""))