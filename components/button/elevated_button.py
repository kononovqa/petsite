import flet as ft

from components.icon.icon import Icons


class ElevatedButtons:
    def __init__(self):
        self.elevated_button_switch_mode = ft.ElevatedButton(
            width=75,
            height=75,
            disabled=False
        )
