from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image as CoreImage
from kivy.uix.progressbar import ProgressBar
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.base import stopTouchApp

from utilities import ScrButton, RoundedButton, TransparentButton


class MainMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (0.431, 0.412, 0.263, 1)
        main_vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
        game_title = Label(text='название_игры', font_family='Arial', italic=True, font_size=24)
        logo = CoreImage(source='assets/images/logo.png')
        copywright = Label(text='(с) копирайтик', size_hint=(1, 0.3), italic=True, font_family='Arial')
        exit_btn = RoundedButton(background_normal='assets/images/btn_normal.png',
                                 background_down='assets/images/btn_down.png',
                                 border_radius=20, text="Выйти", size_hint=(0.75, 0.75), pos_hint={'center_x': 0.5})
        exit_btn.on_press = stopTouchApp

        main_vl.add_widget(game_title)
        main_vl.add_widget(logo)
        main_vl.add_widget(ScrButton(self, direction='left', goal='intro',
                                     background_normal='assets/images/btn_normal.png',
                                     background_down='assets/images/btn_down.png', border_radius=20,
                                     text="Начать с начала",
                                     size_hint=(0.75, 0.75), pos_hint={'center_x': 0.5}))
        main_vl.add_widget(ScrButton(self, direction='left', goal='gameplay',
                                     background_normal='assets/images/btn_normal.png',
                                     background_down='assets/images/btn_down.png', border_radius=20, text="Продолжить",
                                     size_hint=(0.75, 0.75), pos_hint={'center_x': 0.5}))
        main_vl.add_widget(ScrButton(self, direction='right', goal='help',
                                     background_normal='assets/images/btn_normal.png',
                                     background_down='assets/images/btn_down.png', border_radius=20, text="Помощь",
                                     size_hint=(0.75, 0.75), pos_hint={'center_x': 0.5}))
        main_vl.add_widget(exit_btn)
        main_vl.add_widget(copywright)
        self.add_widget(main_vl)


class Intro(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.previous_intro_text = -1
        self.intro_slides = ['Вструпительный текст \nповествующий об игровом \nсеттинге.', 'Ещё один \nслайд.',
                             'Последний слайд.']
        main_vl = BoxLayout(orientation='vertical')
        top_text = Label(text='Введение', font_family='Arial', size_hint=(1, 0.15))

        slides_hl = BoxLayout()
        self.intro_text = Label(text=self.intro_slides[0], italic=True,
                                font_family='Arial', size_hint=(0.6, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                halign='center')
        self.back_btn = TransparentButton(text='<', size_hint=(0.1, 1), pos_hint={'left': 1})
        self.back_btn.on_press = self.intro_back
        self.forward_btn = TransparentButton(text='>', size_hint=(0.1, 1), pos_hint={'right': 1})
        self.forward_btn.on_press = self.intro_forward
        start_btn = ScrButton(self, direction='left', goal='gameplay', text='Начать', size_hint=(1, 0.15),
                              background_normal='', background_down='')
        start_btn.background_color = '#935743'

        main_vl.add_widget(top_text)
        slides_hl.add_widget(self.back_btn)
        slides_hl.add_widget(self.intro_text)
        slides_hl.add_widget(self.forward_btn)
        main_vl.add_widget(slides_hl)
        main_vl.add_widget(start_btn)
        self.add_widget(main_vl)

    def intro_back(self):
        if self.previous_intro_text >= 0:
            self.intro_text.text = self.intro_slides[self.previous_intro_text]
            self.previous_intro_text -= 1

    def intro_forward(self):
        if self.previous_intro_text + 2 < len(self.intro_slides):
            self.intro_text.text = self.intro_slides[self.previous_intro_text + 2]
            self.previous_intro_text += 1


class Gameplay(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
        btns_hl = BoxLayout()
        quests_hl = BoxLayout(size_hint=(1, 0.5))
        resources_hl = BoxLayout(spacing=4, size_hint=(1, 0.35))
        resource1_label = Label(text='0', font_family='Arial', size_hint=(1, 0.25),pos_hint={'center_y': 0.5})
        resource2_label = Label(text='0', font_family='Arial', size_hint=(1, 0.25),pos_hint={'center_y': 0.5})
        resource3_label = Label(text='0', font_family='Arial', size_hint=(1, 0.25),pos_hint={'center_y': 0.5})
        resource4_label = Label(text='0', font_family='Arial', size_hint=(1, 0.25),pos_hint={'center_y': 0.5})
        event_image = CoreImage(source='assets/images/image1.png')
        character_name = Label(text='Имя персонажа', size_hint=(1, 0.3), italic=True, font_family='Arial')
        dialog = Label(text='Диалоговый текст', size_hint=(1, 0.3), italic=True, font_family='Arial')

        action1 = RoundedButton(background_normal='assets/images/btn_normal2.png',
                                background_down='assets/images/btn_down2.png', border_radius=14,
                                text='Действие А', size_hint=(0.5, 0.3), pos_hint={'right': 1})
        action1.on_press = self.action1_handler
        action2 = RoundedButton(background_normal='assets/images/btn_normal2.png',
                                background_down='assets/images/btn_down2.png', border_radius=14,
                                text='Действие Б', size_hint=(0.5, 0.3), pos_hint={'right': 1})
        action2.on_press = self.action2_handler

        quests_label = Label(text='Задания', font_family='Arial', size_hint=(0.8, 0.3),
                             pos_hint={'center_x': 0.5, 'center_y': 0.5})
        back_to_menu = ScrButton(self, direction='right', goal='main_menu',
                                 background_normal='assets/images/btn_normal2.png',
                                 background_down='assets/images/btn_down2.png',border_radius=14,  text='меню',
                                 size_hint=(0.2, 0.7), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        quests_hl.add_widget(back_to_menu)
        quests_hl.add_widget(quests_label)

        resources_hl.add_widget(resource1_label)
        resources_hl.add_widget(resource2_label)
        resources_hl.add_widget(resource3_label)
        resources_hl.add_widget(resource4_label)

        main_vl.add_widget(resources_hl)
        main_vl.add_widget(event_image)
        main_vl.add_widget(character_name)
        main_vl.add_widget(dialog)
        btns_hl.add_widget(action1)
        btns_hl.add_widget(action2)
        main_vl.add_widget(btns_hl)
        main_vl.add_widget(quests_hl)
        self.add_widget(main_vl)

    def action1_handler(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'ending'

    def action2_handler(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'chapter_end'


class ChapterEnd(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
        nav_btns = BoxLayout(size_hint=(1, 0.3))
        nav_btns.background_color = (102, 102, 51, 1)
        statusbar_hl = BoxLayout(size_hint=(1, 0.5))
        choices_btn = RoundedButton(text='решения', size_hint=(0.33, 1),
                                    background_normal='assets/images/btn_normal2.png',
                                    background_down='assets/images/btn_down2.png', border_radius=14)
        statstics_btn = RoundedButton(text='статистика', size_hint=(0.33, 1),
                                      background_normal='assets/images/btn_normal2.png',
                                      background_down='assets/images/btn_down2.png', border_radius=14)
        menu_btn = ScrButton(self, direction='right', goal='main_menu', text='меню', size_hint=(0.33, 1),
                             background_normal='assets/images/btn_normal2.png',
                             background_down='assets/images/btn_down2.png', border_radius=14)

        capter_image = CoreImage(source='assets/images/image2.png')
        chapter_title = Label(text='Конец главы', size_hint=(1, 0.3), italic=True, font_family='Arial')

        timeline = ProgressBar(max=10, size_hint=(0.8, None), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        timeline.value = 3

        character_name = Label(text='Имя персонажа \nВозраст или \nроль персонажа', size_hint=(1, 0.3), italic=True,
                               font_family='Arial', pos_hint={'center_x': 0.3, 'center_y': 0.5})

        status_label = Label(text='Задания', font_family='Arial', size_hint=(0.8, 0.3),
                             pos_hint={'center_x': 0.5, 'center_y': 0.5})
        start_btn = ScrButton(self, direction='left', goal='gameplay', text='Начать', size_hint=(0.2, 0.7),
                              background_normal='assets/images/btn_normal2.png',
                              background_down='assets/images/btn_down2.png', border_radius=14)

        nav_btns.add_widget(choices_btn)
        nav_btns.add_widget(statstics_btn)
        nav_btns.add_widget(menu_btn)
        main_vl.add_widget(nav_btns)
        main_vl.add_widget(capter_image)
        main_vl.add_widget(chapter_title)
        main_vl.add_widget(timeline)
        main_vl.add_widget(character_name)
        statusbar_hl.add_widget(status_label)
        statusbar_hl.add_widget(start_btn)
        main_vl.add_widget(statusbar_hl)
        self.add_widget(main_vl)


class Ending(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.carma = 0
        main_vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
        nav_bar = BoxLayout(size_hint=(1, 0.08))
        carma_label = Label(text='Карма: '+str(self.carma), font_family='Arial', size_hint=(1, 0.12))
        ending_image = CoreImage(source='assets/images/image3.png', size_hint=(1, 0.25))
        ending_text = Label(text='Описание концовки', size_hint=(1, 0.3), italic=True, font_family='Arial')
        restart = ScrButton(self, direction='left', goal='intro',
                            background_normal='assets/images/btn_normal2.png',
                            background_down='assets/images/btn_down2.png', border_radius=14,
                            text='рестарт', size_hint=(0.5, 1))
        back_to_menu = ScrButton(self, direction='right', goal='main_menu',
                                 background_normal='assets/images/btn_normal2.png',
                                 background_down='assets/images/btn_down2.png', border_radius=14,
                                 text='меню', size_hint=(0.5, 1))

        main_vl.add_widget(carma_label)
        main_vl.add_widget(ending_image)
        main_vl.add_widget(ending_text)
        nav_bar.add_widget(back_to_menu)
        nav_bar.add_widget(restart)
        main_vl.add_widget(nav_bar)
        self.add_widget(main_vl)


class Help(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        super().__init__(**kwargs)
        main_vl = BoxLayout(orientation='vertical')
        top_text = Label(text='Помощь по управлению', font_family='Arial', size_hint=(1, 0.15))
        back_to_menu = ScrButton(self, direction='left', goal='main_menu', text='Назад в меню', size_hint=(1, 0.15),
                                 background_normal='', background_down='')
        back_to_menu.background_color = '#935743'

        self.help_text = Label(text='Инструкции по управлению в игре ' * 100, size_hint_y=None, font_size='14sp',
                               italic=True, font_family='Arial', halign='center')
        self.help_text.bind(size=self.resize)
        self.scroll_help = ScrollView(size_hint=(0.8, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.scroll_help.add_widget(self.help_text)

        main_vl.add_widget(top_text)
        main_vl.add_widget(self.scroll_help)
        main_vl.add_widget(back_to_menu)
        self.add_widget(main_vl)

    def resize(self, *args):
        self.help_text.text_size = (self.help_text.width, None)
        self.help_text.texture_update()
        self.help_text.height = self.help_text.texture_size[1]
