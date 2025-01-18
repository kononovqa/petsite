import flet as ft

from components.text.text import Texts


class TextButtons:
    def __init__(self):
        self.text_button = ft.TextButton()


    def get_button_main(self):
        self.text_button.content = Texts().txt_header_main()
        return self.text_button

    def get_button_contacts(self):
        self.text_button.content = Texts().txt_header_contacts()
        return self.text_button

    def get_button_pets(self):
        self.text_button.content = Texts().txt_header_pets()
        return self.text_button

    def get_button_help(self):
        self.text_button.content = Texts().txt_header_help()
        return self.text_button

    def get_button_info(self):
        self.text_button.content = Texts().txt_header_info()
        return self.text_button
