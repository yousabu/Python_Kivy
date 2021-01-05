from kivy.app import App
from kivy.lang import Builder

kv = '''
AnchorLayout:
    canvas:
        Color :
            rgb:1.1.3
        Rectangle:
            pos:self.pos
            size:self.size 
    AsyncImage:
        size_hint:None , None
        size: dp(56) , dp(56)
        source : 'C:\Users\Youssef\Desktop\to.jpg'
        anim_dalay : 0.0

'''
class TestApp(App):
    def build(self):
        return Builder.load_string(kv)

if __name__=='__main__':
    TestApp().run()