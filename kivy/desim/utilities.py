from kivy.uix.button import Button


class ScrButton(Button):
    def __init__(self, screen, direction='right', goal='main', border_radius=None,
                 background_normal=None,
                 background_down=None, **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
        if background_normal is not None:
            self.background_normal = background_normal
        if background_down is not None:
            self.background_down = background_down
        if border_radius is not None:
            self.border = (border_radius, border_radius, border_radius, border_radius)

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal


class RoundedButton(Button):
    def __init__(self, border_radius=20, background_normal='assets/images/btn_normal.png',
                 background_down='assets/images/btn_down.png', **kwargs):
        super().__init__(**kwargs)
        self.background_normal = background_normal
        self.background_down = background_down
        self.border = (border_radius, border_radius, border_radius, border_radius)


class TransparentButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_down = ''
        self.background_color = (0, 0, 0, 0)
