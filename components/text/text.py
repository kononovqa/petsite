import flet as ft


class Texts:
    def __init__(self):
        self.txt_main_text = ft.Text(value='',
                                     font_family='Arial',
                                     size=22,
                                     color=ft.Theme.primary_color_dark)

        self.txt_card_text = ft.Text(value='',
                                     weight=ft.FontWeight.W_600,
                                     font_family='Rubik',
                                     size=20,
                                     color=ft.Theme.primary_color_dark)

    def txt_header_main(self):
        self.txt_main_text.value = 'Главная'
        return self.txt_main_text

    def txt_header_contacts(self):
        self.txt_main_text.value = 'Контакты'
        return self.txt_main_text

    def txt_name_card(self):
        self.txt_card_text.value = 'Вася'
        return self.txt_card_text

    def txt_name_card_2(self):
        self.txt_card_text.value = '1234567890 123456'
        return self.txt_card_text
