import flet as ft


class Columns:
    def __init__(self):
        self.row_cards = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
            run_spacing=0
        )
