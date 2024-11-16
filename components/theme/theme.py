import flet as ft


class Theme:

    def __init__(self):
        self.dark_theme = ft.Theme(
            color_scheme=ft.ColorScheme(primary="#E5E6E8",
                                        background="#1D1A20"),
            appbar_theme=ft.AppBarTheme(bgcolor="#1D1A20")

        )
        self.light_theme = ft.Theme(
            color_scheme=ft.ColorScheme(primary="#1D1A20",
                                        background="#E5E6E8"),
            appbar_theme=ft.AppBarTheme(bgcolor="#E5E6E8")
        )