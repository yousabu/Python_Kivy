from kivy.uix.accordion import Accordion ,AccordionItem
from kivy.uix.label import Label
from kivy.app import App


class AccordionApp(App):
    def build(self):
        root =Accordion()
        for x in range(5):
            item = AccordionItem(title='Title %d'  %x , min_space=60)
            item.add_widget(Label(text='Hello Youssef \n' *5))
            root.add_widget(item)
        return root


if __name__ == '__main__':
    AccordionApp().run()