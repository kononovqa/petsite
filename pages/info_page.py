import copy

import flet as ft

from components.column.column import Columns
from components.row.row import Rows
from components.text.text import Texts
from data.test_data import test_description


def info_page(page, width = 0, height = 0):
    row_elements_info = Rows().row_elements
    def color_blue(e):
        print(e)

    def txt_blue(e):
        if e.data == 'true':
            e.control.content.color = '#68E3FF'
            e.control.border = ft.border.all(0.5, '#68E3FF')
        elif e.data == 'false':
            e.control.content.color = ft.Colors.PRIMARY
            e.control.border = ft.border.all(0.5, ft.Colors.PRIMARY)
        page.update()


    def close(e):
        page.dialog.open = False


    def open_descript(e):
        description = ft.Text(value=test_description)
        page.dialog = ft.AlertDialog(title=ft.Text(e.control.content.value),
                                     on_dismiss=close,
                                     content=description)
        page.dialog.open = True
        page.update()


    quest_txt = Texts().txt_quest()
    quest_txt.spans = [ft.TextSpan(url='https://www.google.ru/',
                                   on_enter=color_blue,
                                   )]

    container_quest = ft.Container(
        padding=0,
        margin=0,
        on_hover=txt_blue,
        on_click=open_descript,
        #bgcolor=ft.Colors.RED,
        border_radius=12,
        border=ft.border.all(0.5, ft.Colors.PRIMARY),
        alignment=ft.alignment.center,
        width=450,
        height=100)

    stack_info = ft.Stack(
        controls=[container_quest],
        width=450,
        height=110)

    container_quest.content = quest_txt

    row_elements_info.controls.append(copy.deepcopy(stack_info))
    row_elements_info.controls.append(copy.deepcopy(stack_info))
    row_elements_info.controls.append(copy.deepcopy(stack_info))
    row_elements_info.controls.append(copy.deepcopy(stack_info))

    row_cards = Columns().row_cards
    row_cards.controls = [ft.Row(height=22), row_elements_info]
    content = row_cards

    def resize(width_page, height_page):
        None

        page.update()
    if width == 0 or height == 0:
        width = int(page.width)
        height = int(page.height)
    resize(width, height)

    return content

