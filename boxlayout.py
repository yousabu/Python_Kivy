from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

runTouchApp( Builder.load_string("""

BoxLayout:
    orientation: 'vertical'
    spacing : 10
    padding :5
    Button:
        text:'B1'
    Button:
        text:'B1'
    Button:
        text:'B1'


"""))    

# class MyList(BoxLayout):
#     pass

# if __name__ == '__main__':
#         runTouchApp(MyList())