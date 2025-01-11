import random

import flet as ft

from config.settings import ADDRESS, PHONE, CALENDAR


class Texts:
    def __init__(self):
        self.txt_main_text = ft.Text(value='',
                                     font_family='Arial',
                                     size=22,
                                     color=ft.Theme.primary_color_dark)

        self.txt_card_name_text = ft.Text(value='',
                                          size=23,
                                          color=ft.Theme.primary_color_dark)

        self.txt_age = ft.Text(value='',
                               font_family='NotoSansBold',
                               size=18)

        self.txt_main_text = ft.Text(value='',
                                     font_family='Arial',
                                     size=20,
                                     color=ft.Theme.primary_color_dark)

        self.txt_side_text = ft.Text(value='',
                                     font_family='Arial',
                                     size=16,
                                     color=ft.Theme.primary_color_dark)

    def txt_header_main(self):
        self.txt_main_text.value = 'Главная'
        return self.txt_main_text

    def txt_header_contacts(self):
        self.txt_main_text.value = 'Контакты'
        return self.txt_main_text

    def txt_header_pets(self):
        self.txt_main_text.value = 'Выбрать питомца'
        return self.txt_main_text

    def txt_header_help(self):
        self.txt_main_text.value = 'Помочь'
        return self.txt_main_text

    def txt_name_card(self):
        list_names = ['Вася', 'Дафна', 'Степа']
        self.txt_card_name_text.value = random.choice(list_names)
        self.txt_card_name_text.font_family = 'NotoSansBold'
        return self.txt_card_name_text

    def txt_description_card(self):
        list_description = ['Я вася проказник, у меня грустное лицо но '
                            'веселый характер',
                            'Дафна веселый корги, который не против поиграть с '
                            'твоим ботинком)',
                            'Степа дружелюбный парень, обожает бегать за мячиком по утрам'
                            ]
        self.txt_card_name_text.value = random.choice(list_description)
        self.txt_card_name_text.size = 14
        self.txt_card_name_text.font_family = 'NotoSansRegular'
        return self.txt_card_name_text

    def txt_main_address(self):
        self.txt_main_text.value = 'Наши контакты'
        return self.txt_main_text

    def txt_main_map(self):
        self.txt_main_text.value = 'Мы на карте'
        return self.txt_main_text

    def txt_side_address(self):
        self.txt_side_text.value = ADDRESS
        return self.txt_side_text

    def txt_side_phone(self):
        self.txt_side_text.value = PHONE
        return self.txt_side_text

    def txt_side_time_work(self):
        self.txt_side_text.value = CALENDAR
        return self.txt_side_text