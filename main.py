from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer

from kivy.config import Config

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '400')

from kivy.uix.floatlayout import FloatLayout

class MyApp(App):
    def build(self):

        fl = FloatLayout(size = (600, 400))

        fl.add_widget(Button(
            text = "Button", 
            on_press = self.btn_press,
            background_color = [1, 0, 0, 1],
            background_normal = '',
            size_hint = (.5, .25),
            pos = (50, 50)))
        
        return fl

    def btn_press(self, instance):
        print('кнопка нажата')
        instance.text = 'НАЖАТА'
if __name__=="__main__":
    MyApp().run()