import flet as ft

from components.button.icon_button import IconButtons
from components.button.text_button import TextButtons
from components.icon.icon import Icons
from components.stack.stack import Stacks
from components.theme.theme import Theme
from components.progress_bar.progress_bar import ProgressBars
from components.container.container import Containers


def main_page(page):

    async def go_main_page(e):
        page.go('/')

    async def go_contacts_page(e):
        page.go('/contacts')

    async def change_theme(e):
        if page.theme_mode == "light":
            page.theme_mode = "dark"
            page.dark_theme = Theme().dark_theme
            page.bgcolor = "#1D1A20"

        elif page.theme_mode == "dark":
            page.theme_mode = "light"
            page.theme = Theme().light_theme
            page.bgcolor = "#E5E6E8"

        button_switch_theme.icon = Icons().icon_light_theme \
            if page.theme_mode == "dark" else Icons().icon_dark_theme
        page.update()

    button_switch_theme = IconButtons().get_button_switch_theme()
    button_switch_theme.on_click = change_theme

    button_main = TextButtons().get_button_main()
    button_main.on_click = go_main_page

    button_contacts = TextButtons().get_button_contacts()
    button_contacts.on_click = go_contacts_page

    horizontal_divider_header = Containers().horizontal_divider
    horizontal_divider_header.alignment = ft.alignment.bottom_center

    row_horizontal_divider_header = ft.Row(
        [horizontal_divider_header],
        height=1,
        spacing=0,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.alignment.bottom_center)

    row_header = ft.Row(
        [button_main, ProgressBars().vertical_divider, button_contacts],
        height=59,
        spacing=0,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.alignment.center)

    row_button_switch_theme = ft.Row([button_switch_theme],
                                     height=59,
                                     width=int(page.width)-20,
                                     alignment=ft.MainAxisAlignment.END,
                                     vertical_alignment=ft.alignment.center)

    stack_app_bar = Stacks().stack_app_bar()
    stack_app_bar.controls = [row_header, row_button_switch_theme]
    stack_app_bar.height = 59

    page.appbar = ft.AppBar(
        title=ft.Column([
            stack_app_bar,
            row_horizontal_divider_header
        ], spacing=0),
        bgcolor=ft.Theme.appbar_theme,
        toolbar_height=60,
        title_spacing=0)


    row_cards = ft.Row([
            ft.Stack([
                ft.Container(
                    bgcolor=ft.colors.RED,
                    width=220,
                    height=220),
                ft.Container(
                    bgcolor=ft.colors.GREY,
                    width=220,
                    height=100,
                    bottom=0)
                ],
            width=220,
            height=320,
            col={"xs": 6, "sm": 6, "md": 4, "xl": 2, 'xxl': 2},
            alignment=ft.alignment.top_center,
            ),
            ft.Stack([
                ft.Container(
                    bgcolor=ft.colors.GREEN,
                    width=220,
                    height=220),
                ft.Container(
                    bgcolor=ft.colors.GREY,
                    width=220,
                    height=100,
                    bottom=0)
                    ],
                width=220,
                height=320,
                col={"xs": 6, "sm": 6, "md": 4, "xl": 2, 'xxl': 2},
                alignment=ft.alignment.top_center,
            ),

            ft.Stack([
                ft.Container(
                    bgcolor=ft.colors.BLUE,
                    width=220,
                    height=220),
                ft.Container(
                    bgcolor=ft.colors.GREY,
                    width=220,
                    height=100,
                    bottom=0)
            ],
                width=220,
                height=320,
                col={"xs": 6, "sm": 6, "md": 4, "xl": 2, 'xxl': 2},
                alignment=ft.alignment.top_center,
            ),
            ft.Stack([
                ft.Container(
                    bgcolor=ft.colors.WHITE,
                    width=220,
                    height=220),
                ft.Container(
                    bgcolor=ft.colors.GREY,
                    width=220,
                    height=100,
                    bottom=0)
            ],
                width=220,
                height=320,
                col={"xs": 6, "sm": 6, "md": 4, "xl": 2, 'xxl': 2},
                alignment=ft.alignment.top_center,
            ),

            ft.Stack([
                ft.Container(
                    bgcolor=ft.colors.PURPLE,
                    width=220,
                    height=220),
                ft.Container(
                    bgcolor=ft.colors.GREY,
                    width=220,
                    height=100,
                    bottom=0)
            ],
                width=220,
                height=320,
                col={"xs": 6, "sm": 6, "md": 4, "xl": 2, 'xxl': 2},
                alignment=ft.alignment.top_center,
            ),

            ft.Stack([
                ft.Container(
                    bgcolor=ft.colors.ORANGE,
                    width=220,
                    height=220),
                ft.Container(
                    bgcolor=ft.colors.GREY,
                    width=220,
                    height=100,
                    bottom=0)
            ],
                width=220,
                height=320,
                col={"xs": 6, "sm": 6, "md": 4, "xl": 2, 'xxl': 2},
                alignment=ft.alignment.top_center,
            ),

            ft.Stack([
                ft.Container(
                    bgcolor=ft.colors.CYAN,
                    width=220,
                    height=220),
                ft.Container(
                    bgcolor=ft.colors.GREY,
                    width=220,
                    height=100,
                    bottom=0)
            ],
                width=220,
                height=320,
                col={"xs": 6, "sm": 6, "md": 4, "xl": 2, 'xxl': 2},
                alignment=ft.alignment.top_center,
            ),
        ],
        width=1490,
        vertical_alignment=ft.alignment.center,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=24,
        run_spacing=24)
    content = row_cards

    def resize(width, height):
        horizontal_divider_header.width = width - 40
        row_button_switch_theme.width = width - 20


    def page_resized(e):
        width_page = int(e.width)
        height_page = int(e.height)
        resize(width = width_page, height=height_page)
        page.update()

    resize(int(page.width), int(page.height))
    page.on_resized = page_resized

    return content
