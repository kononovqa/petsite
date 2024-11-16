import flet as ft

from components.icon.icon import Icons


class IconButtons:
    def __init__(self):
        self.button_icon = ft.IconButton(
            icon_color=ft.Theme.appbar_theme)

    def get_button_switch_theme(self):
        self.button_icon.icon = Icons().icon_light_theme
        self.button_icon.icon_size = 32
        self.button_icon.height = 59
        return self.button_icon

    def icon_switch_theme_to_dark(self):
        self.button_icon.icon = Icons().icon_dark_theme
        return self.button_icon

    def icon_switch_theme_to_light(self):
        self.button_icon.icon = Icons().icon_light_theme
        return self.button_icon
