import copy
import flet as ft

from components.button.icon_button import IconButtons
from components.button.text_button import TextButtons
from components.icon.icon import Icons
from components.stack.stack import Stacks
from components.progress_bar.progress_bar import ProgressBars
from components.container.container import Containers
from components.text.text import Texts


def main_page(page):

    async def go_main_page(e):
        page.go('/')

    async def go_contacts_page(e):
        page.go('/contacts')

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

    row_elements = ft.Row([],
        wrap=True,
        width=1490,
        vertical_alignment=ft.alignment.center,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=24,
        run_spacing=24)

    def next_pict(e):
        index = e.control.data
        count = int(list_images_object[index].src.split('.')[0])
        list_images_object[index].src = f'{count+1}.jpg'
        list_move_right_object[index].data = index
        page.update()

    def prev_pict(e):
        index = e.control.data
        count = int(list_images_object[index].src.split('.')[0])
        list_images_object[index].src = f'{count - 1}.jpg'
        list_move_left_object[index].data = index
        page.update()

    move_right = IconButtons().move_right_image()
    move_right.on_click = next_pict

    move_left = IconButtons().move_left_image()
    move_left.on_click = prev_pict

    image = ft.Image(src=f'',
                     right=1,
                     left=1,
                     bottom=1,
                     top=1)

    list_images_object = []
    list_move_right_object = []
    list_move_left_object = []

    for a in range(7):
        stack_animals = ft.Stack(width=220, height=332)

        image = copy.deepcopy(image)
        image.src = f'{a + 1}.jpg'
        list_images_object.append(image)

        move_right = copy.deepcopy(move_right)
        move_right.data = a
        list_move_right_object.append(move_right)

        move_left = copy.deepcopy(move_left)
        move_left.data = a
        list_move_left_object.append(move_left)

        container_pict_animals = ft.Container(
                        ft.Stack([image,
                                         move_right,
                                         move_left],
                                         width=220,
                                         height=220),
                        bgcolor=ft.Colors.ON_SECONDARY,
                        border_radius=12,
                        border=ft.border.all(0.5, ft.Colors.PRIMARY),
                        width=220,
                        height=220)

        container_description_animals = (
            ft.Container(
                        content=ft.Stack([
                            ft.Container(Texts().txt_name_card(),
                                         width=220,
                                         height=60,
                                         alignment=ft.alignment.center,
                                         top=1),
                            ft.Container(
                                content=ft.Row([
                                    ft.CircleAvatar(foreground_image_src='bordo.jpg',
                                                     height=30,
                                                     width=30),
                                    ft.CircleAvatar(foreground_image_src='garage.png',
                                                    height=30,
                                                    width=30),
                                    ft.CircleAvatar(content=ft.Text('13',
                                                                    color=ft.Colors.PRIMARY),
                                                    bgcolor=ft.Colors.OUTLINE,
                                                    height=30,
                                                    width=30),
                                    ft.CircleAvatar(content=ft.Text('1',
                                                                    color=ft.Colors.PRIMARY),
                                                    bgcolor=ft.Colors.OUTLINE,
                                                    height=30,
                                                    width=30),
                                    ft.CircleAvatar(content=ft.Text('70',
                                                                    color=ft.Colors.PRIMARY),
                                                    bgcolor=ft.Colors.OUTLINE,
                                                    height=30,
                                                    width=30),
                                    ft.CircleAvatar(content=ft.Text('0',
                                                                    color=ft.Colors.PRIMARY),
                                                    bgcolor=ft.Colors.OUTLINE,
                                                    height=30,
                                                    width=30),
                                ], spacing=5, alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                 height=50,
                                 width=220,
                                 bottom=0)
                        ]),
                        bgcolor=ft.Colors.ON_SECONDARY,
                        border_radius=12,
                        border=ft.border.all(0.5, ft.Colors.PRIMARY),
                        width=220,
                        height=100,
                        bottom=0))

        stack_animals.controls.append(container_pict_animals)
        stack_animals.controls.append(container_description_animals)
        row_elements.controls.append(stack_animals)

    row_cards = ft.Column([
        ft.Row(height=22),
        row_elements],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=0,
        run_spacing=0
    )
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
