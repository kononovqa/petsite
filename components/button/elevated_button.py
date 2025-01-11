import flet as ft

from components.icon.icon import Icons


class ElevatedButtons:
    def __init__(self):
        self.elevated_button_switch_mode = ft.ElevatedButton(
            width=75,
            height=75,
            disabled=False
        )

        self.icon_move = ft.TextButton(
            #icon_color=ft.Colors.TRANSPARENT,
            #bgcolor=ft.Colors.TRANSPARENT,
            height=220,
            width=50,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12),
                                 padding=ft.padding.all(0)))

    def move_right_image(self):
        self.icon_move.content = Icons().icon_move_right
        self.icon_move.right = 1
        return self.icon_move

    def move_left_image(self):
        self.icon_move.content = Icons().icon_move_left
        self.icon_move.left = 1
        return self.icon_move