import flet as ft

from components.icon.icon import Icons
from config.settings import ADDRESS, PHONE, CALENDAR


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

    def icon_copy(self):
        self.button_icon.icon = Icons().icon_copy
        self.button_icon.icon_size = 22
        self.button_icon.data = ADDRESS
        return self.button_icon

    def icon_phone(self):
        self.button_icon.icon = Icons().icon_phone
        self.button_icon.icon_size = 22
        self.button_icon.data = PHONE
        return self.button_icon

    def icon_calendar(self):
        self.button_icon.icon = Icons().icon_calendar
        self.button_icon.icon_size = 22
        self.button_icon.data = CALENDAR
        return self.button_icon
