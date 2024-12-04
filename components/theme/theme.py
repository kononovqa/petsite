import flet as ft


class Theme:

    def __init__(self):
        self.dark_theme = ft.Theme(
            color_scheme=ft.ColorScheme(primary="#E5E6E8",
                                        on_secondary='#232026',
                                        background="#1D1A20",
                                        outline='#7a6869',
                                        ),
            appbar_theme=ft.AppBarTheme(bgcolor="#1D1A20")

        )
        self.light_theme = ft.Theme(
            color_scheme=ft.ColorScheme(primary="#1D1A20",
                                        on_secondary='#e1e1e3',
                                        background="#E5E6E8",
                                        outline='#878787',
                                        ),
            appbar_theme=ft.AppBarTheme(bgcolor="#E5E6E8")
        )