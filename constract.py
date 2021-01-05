from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.button import Button

class Class1(BoxLayout):
    def __init__(self, **kwargs):
        super(Class1,self).__init__(**kwargs)
        button = Button(text='Youssef Abu-hamda')    
        self.add_widget(button)
        self.padding=10

class Class2(App):
    def build(self):
        return Class1()

if __name__=='__main__':
    Class2().run()
