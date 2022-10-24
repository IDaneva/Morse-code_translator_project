from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Morse_Translator(Widget):
    pass


class MorseApp(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 2
        self.window.rows = 3
        self.add_text =Label(text="Please enter the text in morse:")
        self.window.add_widget(self.add_text)
        self.user = TextInput(multiline=True)
        self.window.add_widget(self.user)
        self.button = Button(text="Translate!")
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)


    def callback(self, instance):
        self.add_text.text = "HI i should add the morse translating logic here"


        return self.window


if __name__ == '__main__':
    MorseApp().run()


morse_alphabet = {".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e",
                  "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j",
                  "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o",
                  ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t",
                  "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z"}


from kivy.uix.textinput import TextInput
textinput = TextInput(text='Hello world')
