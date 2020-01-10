from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 284)
Config.set('graphics', 'height', 454)

class CalcApp(App):
    def clear (self):
        pass
    def clear_all (self):
        pass

    def add_operation(self, instance):
        if ( str(instance.text).lower() == 'x'):
            self.formula += '*'
        else:
            self.formula += str(instance.text)
        self.input_label.text = self.formula
        self.сurrent_number = '0'
        self.update_label()       
    def update_label(self):
        self.result.text = self.сurrent_number     
    def add_formula(self, instance):
        if (self.сurrent_number == '0'):
                self.сurrent_number = ''
        self.formula += str(instance.text)
        self.сurrent_number += str(instance.text)
        self.update_label()

    def calc_result(self, instance):
        self.input_label.text = self.formula
        self.result.text = str(eval(self.formula))
        self.formula = self.result.text
        self.formula = ''
        self.сurrent_number = ''

    def build(self):
        self.сurrent_number = ''
        self.formula = ''
        layout = BoxLayout(orientation='vertical', padding=[2])
        input_panel = GridLayout(cols=4, size_hint=(None, None), size=(280, 350))
        result_panel = GridLayout(rows=2, size_hint=(None, None), size=(280, 100))

        self.input_label = Label(text='1',
            font_size = 40,
            size_hint=(None, None),
            size=(280, 50),
            halign='right',
            valign='top',
            text_size=(280, 50))
        self.result = Label(text='0',
            font_size = 50,
            size_hint=(None, None),
            size=(280, 50),
            halign='right',
            valign='bottom',
            text_size=(280, 50))
        result_panel.add_widget( self.input_label )        
        result_panel.add_widget( self.result )

        input_panel.add_widget( Button(text = '<', on_press = self.add_formula) )
        input_panel.add_widget( Button(text = 'CE', on_press = self.clear) )
        input_panel.add_widget( Button(text = 'C', on_press = self.clear_all) )
        input_panel.add_widget( Button(text = '/', on_press = self.add_operation) )

        input_panel.add_widget( Button(text = '7', on_press = self.add_formula) )
        input_panel.add_widget( Button(text = '8', on_press = self.add_formula) )
        input_panel.add_widget( Button(text = '9', on_press = self.add_formula) )
        input_panel.add_widget( Button(text = 'X', on_press = self.add_operation) )

        input_panel.add_widget( Button(text = '4', on_press = self.add_formula) )
        input_panel.add_widget( Button(text = '5', on_press = self.add_formula) )
        input_panel.add_widget( Button(text = '6', on_press = self.add_formula) )
        input_panel.add_widget( Button(text = '-', on_press = self.add_operation) )

        input_panel.add_widget( Button(text = '1', on_press = self.add_formula) )
        input_panel.add_widget( Button(text = '2', on_press = self.add_formula) )
        input_panel.add_widget( Button(text = '3', on_press = self.add_formula) )
        input_panel.add_widget( Button(text = '+', on_press = self.add_operation) )

        input_panel.add_widget( Widget() )
        input_panel.add_widget( Button(text = '0', on_press = self.add_formula) )
        input_panel.add_widget( Button(text = '.', on_press = self.add_formula) )
        input_panel.add_widget( Button(text = '=', on_press = self.calc_result) )

        layout.add_widget(result_panel)
        layout.add_widget(input_panel)
        return layout


if __name__ == "__main__":
    CalcApp().run()