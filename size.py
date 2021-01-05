from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string('''
<Button>:
    Color: .8,.2,0,1
FloatLayout:
    Button:
        text:'He'
        size_hint: 0.2, 0.1
        pos_hint: {'down':.1,'lift':1}




'''))