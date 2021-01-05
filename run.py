from kivy.base import runTouchApp
from kivy.lang import Builder



runTouchApp(Builder.load_string('''
<Button>:
    color: .8,.2,0,1
StackLayout:
    Button:
        text:'S1'
        size_hint: 0.1,0.3


'''))

