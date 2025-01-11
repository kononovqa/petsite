import flet as ft


class Images:
    def __init__(self):
        self.image = ft.Image(src=f'',
                 fit=ft.ImageFit.COVER,
                 width=220,
                 height=220,
                 border_radius=9,
                 )
