import flet as ft


class Rows:
    def __init__(self):
        self.horizontal_divider = ft.Row(
            height=1,
            spacing=0,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.alignment.bottom_center)

        self.row_header = ft.Row(
            height=59,
            spacing=0,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.alignment.center)

        self.row_button_switch_theme = ft.Row(
            height=59,
            alignment=ft.MainAxisAlignment.END,
            vertical_alignment=ft.alignment.center)

        self.row_elements = ft.Row([],
                                   wrap=True,
                                   width=1490,
                                   vertical_alignment=ft.alignment.center,
                                   alignment=ft.MainAxisAlignment.CENTER,
                                   spacing=24,
                                   run_spacing=24)

        self.row_spacing = ft.Row(height=50,
                                  alignment=ft.MainAxisAlignment.CENTER,
                                  vertical_alignment=ft.CrossAxisAlignment.CENTER)

        self.row_little_spacing = ft.Row(height=35,
                                  alignment=ft.MainAxisAlignment.START,
                                  vertical_alignment=ft.CrossAxisAlignment.CENTER)
