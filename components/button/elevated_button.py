import flet as ft

from components.icon.icon import Icons


class ElevatedButtons:
    def __init__(self):
        self.elevated_button_switch_mode = ft.ElevatedButton(
            content='',
            width=75,
            height=75,
            disabled=False
        )

    def icon_switch_theme_to_dark(self):
        self.elevated_button_switch_mode.content = Icons().icon_switch_theme_to_dark
        return self.elevated_button_switch_mode

    def icon_switch_theme_to_light(self):
        self.elevated_button_switch_mode.content = Icons().icon_switch_theme_to_light
        return self.elevated_button_switch_mode


