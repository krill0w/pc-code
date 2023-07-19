from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class RandomiserLogic(GridLayout):
    def __init__(self, **kwargs):
        super(RandomiserLogic, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Number of Players"))
        self.numOfPlayers = TextInput(multiline=False)
        self.add_widget(self.numOfPlayers)
        self.add_widget(Label(text="Number of Tracks"))
        self.numOfTracks = TextInput(multiline=False)
        self.add_widget(self.numOfTracks)


class RandomiserApp(App):
    def build(self):
        return RandomiserLogic()

if __name__ == '__main__':
    RandomiserApp().run()