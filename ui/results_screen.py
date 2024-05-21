from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class ResultsScreen(Screen):
    def __init__(self, **kwargs):
        super(ResultsScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text="Results Screen")
        back_button = Button(text="Back to Main")

        back_button.bind(on_release=self.switch_to_main)

        layout.add_widget(label)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def switch_to_main(self, instance):
        self.manager.current = 'main'
