from kivy.app import App
from kivy.uix.button import Button

class MonApp(App):
    def build(self):
        return Button(text="Salut !")

MonApp().run()
