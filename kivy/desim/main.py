from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens import MainMenu, Intro, Gameplay, ChapterEnd, Help, Ending


class Desim(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu(name='main_menu'))
        sm.add_widget(Intro(name='intro'))
        sm.add_widget(Gameplay(name='gameplay'))
        sm.add_widget(ChapterEnd(name='chapter_end'))
        sm.add_widget(Help(name='help'))
        sm.add_widget(Ending(name='ending'))
        return sm


# Точка входа
if __name__ == '__main__':
    app = Desim()
    app.run()
