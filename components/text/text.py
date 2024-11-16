import flet as ft


class Texts:
    def __init__(self):
        self.txt_main_text = ft.Text(value='',
                                     font_family='Arial',
                                     size=20,
                                     color=ft.Theme.primary_color_dark)

    def txt_header_main(self):
        self.txt_main_text.value = 'Главная'
        return self.txt_main_text

    def txt_header_contacts(self):
        self.txt_main_text.value = 'Контакты'
        return self.txt_main_text
