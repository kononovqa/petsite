import flet as ft


class Containers:
    def __init__(self):
        # start.py
        self.horizontal_divider = ft.Container(
            width=100,
            height=1,
            bgcolor="#857d7f")

        self.container_txt_age = ft.Container(alignment=ft.alignment.center,
                                              width=30,
                                              height=30)
