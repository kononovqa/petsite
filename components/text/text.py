import random

import flet as ft


class Texts:
    def __init__(self):
        self.txt_main_text = ft.Text(value='',
                                     font_family='Arial',
                                     size=22,
                                     color=ft.Theme.primary_color_dark)

        self.txt_card_name_text = ft.Text(value='',
                                          size=23,
                                          color=ft.Theme.primary_color_dark)

    def txt_header_main(self):
        self.txt_main_text.value = 'Главная'
        return self.txt_main_text

    def txt_header_contacts(self):
        self.txt_main_text.value = 'Контакты'
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
