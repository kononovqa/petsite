import flet as ft

from components.button.icon_button import IconButtons
from components.button.text_button import TextButtons
from components.icon.icon import Icons
from components.stack.stack import Stacks
from components.progress_bar.progress_bar import ProgressBars
from components.container.container import Containers
from components.row.row import Rows
from components.appbar.appbar import AppBars


def main_page(page):
    async def go_main_page(e):
        page.go('/')

    async def go_contacts_page(e):
        page.go('/contacts')

    async def go_pets_page(e):
        page.go('/pets')

    async def go_help_page(e):
        page.go('/help')

    async def change_theme(e):
        if page.theme_mode == "light":
            page.theme_mode = "dark"
            page.bgcolor = "#1D1A20"

        elif page.theme_mode == "dark":
            page.theme_mode = "light"
            page.bgcolor = "#E5E6E8"

        button_switch_theme.icon = Icons().icon_light_theme \
            if page.theme_mode == "dark" else Icons().icon_dark_theme
        page.update()

    button_main = TextButtons().get_button_main()
    button_main.on_click = go_main_page

    button_contacts = TextButtons().get_button_contacts()
    button_contacts.on_click = go_contacts_page

    button_pets = TextButtons().get_button_pets()
    button_pets.on_click = go_pets_page

    button_help = TextButtons().get_button_help()
    button_help.on_click = go_help_page

    row_header = Rows().row_header
    vertical_divider = ProgressBars().vertical_divider
    row_header.controls = [button_main, vertical_divider,
                           button_pets, vertical_divider,
                           button_help, vertical_divider,
                           button_contacts]

    button_switch_theme = IconButtons().get_button_switch_theme()
    button_switch_theme.on_click = change_theme

    row_button_switch_theme = Rows().row_button_switch_theme
    row_button_switch_theme.controls = [button_switch_theme]
    row_button_switch_theme.width = int(page.width) - 20

    stack_app_bar = Stacks().stack_app_bar()
    stack_app_bar.controls = [row_header, row_button_switch_theme]
    stack_app_bar.height = 59

    horizontal_divider_header = Containers().horizontal_divider
    horizontal_divider_header.alignment = ft.alignment.bottom_center

    row_horizontal_divider_header = Rows().horizontal_divider
    row_horizontal_divider_header.controls = [horizontal_divider_header]

    appbar = AppBars().appbar
    appbar.title = ft.Column([
        stack_app_bar,
        row_horizontal_divider_header
    ], spacing=0)
    page.appbar = appbar

    def resize(width, height):
        horizontal_divider_header.width = width - 40
        row_button_switch_theme.width = width - 20

    def page_resized(e):
        width_page = int(e.width)
        height_page = int(e.height)
        resize(width=width_page, height=height_page)
        page.update()

    resize(int(page.width), int(page.height))
    page.on_resized = page_resized

