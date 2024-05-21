from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from ui.main_screen import MainScreen
from ui.number_generator_screen import NumberGeneratorScreen
from ui.number_selector_screen import NumberSelectorScreen
from ui.results_screen import ResultsScreen

class LottoApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(MainScreen(name="main"))
        self.screen_manager.add_widget(NumberGeneratorScreen(name="generate"))
        self.screen_manager.add_widget(NumberSelectorScreen(name="select"))
        self.screen_manager.add_widget(ResultsScreen(name="results"))
        return self.screen_manager

if __name__ == "__main__":
    LottoApp().run()
