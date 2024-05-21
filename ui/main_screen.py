from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        generate_button = Button(text="Generate Numbers")
        select_button = Button(text="Select Numbers")
        results_button = Button(text="View Results")

        generate_button.bind(on_release=self.switch_to_generate)
        select_button.bind(on_release=self.switch_to_select)
        results_button.bind(on_release=self.switch_to_results)

        layout.add_widget(generate_button)
        layout.add_widget(select_button)
        layout.add_widget(results_button)

        self.add_widget(layout)

    def switch_to_generate(self, instance):
        self.manager.current = 'generate'

    def switch_to_select(self, instance):
        self.manager.current = 'select'

    def switch_to_results(self, instance):
        self.manager.current = 'results'
