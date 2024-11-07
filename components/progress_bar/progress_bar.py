import flet as ft


class ProgressBars:
    def __init__(self):
        self.vertical_divider = ft.ProgressBar(width=1,
                                               height=22,
                                               value=1,
                                               color="#857d7f")
