import flet as ft


class AppBars:
    def __init__(self):
        self.appbar = ft.AppBar(
            bgcolor=ft.Theme.appbar_theme,
            toolbar_height=60,
            title_spacing=0)

