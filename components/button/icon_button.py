import flet as ft

from components.icon.icon import Icons


class IconButtons:
    def __init__(self):
        self.button_icon = ft.IconButton(
            icon_color=ft.Theme.appbar_theme)

        self.icon_move = ft.IconButton(
            icon_color=ft.Theme.appbar_theme,
            icon_size=32,
            height=220,
            width=50,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12),
                                                padding=ft.padding.all(0)))

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

    def move_right_image(self):
        self.icon_move.icon = Icons().icon_move_right
        self.icon_move.right = 1
        return self.icon_move

    def move_left_image(self):
        self.icon_move.icon = Icons().icon_move_left
        self.icon_move.left = 1
        return self.icon_move
