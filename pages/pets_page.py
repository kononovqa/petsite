import copy
import random

import flet as ft

from components.button.elevated_button import ElevatedButtons
from components.stack.stack import Stacks
from components.container.container import Containers
from components.text.text import Texts
from components.row.row import Rows
from components.image.image import Images
from components.circleavatar.circleavatar import CircleAvatars
from data.random_data import agressive_list, colors_gender
from components.column.column import Columns


def pets_page(page):
    row_elements = Rows().row_elements

    def next_pict(e):
        index = e.control.data
        count = int(list_images_object[index].src.split('.')[0])
        list_images_object[index].src = f'{count + 1}.jpg'
        list_move_right_object[index].data = index
        page.update()

    def prev_pict(e):
        index = e.control.data
        count = int(list_images_object[index].src.split('.')[0])
        list_images_object[index].src = f'{count - 1}.jpg'
        list_move_left_object[index].data = index
        page.update()

    def on_hover_ev(e):
        if e.data == 'true':
            e.control.content.color = ft.Theme.appbar_theme
        elif e.data == 'false':
            e.control.content.color = ft.Colors.TRANSPARENT
        page.update()

    move_right = ElevatedButtons().move_right_image()
    move_right.on_click = next_pict
    move_right.on_hover = on_hover_ev

    move_left = ElevatedButtons().move_left_image()
    move_left.on_click = prev_pict
    move_left.on_hover = on_hover_ev

    image = Images().image

    icon_right = CircleAvatars().icon_right

    def color_text_picker(age: int, age_end: int):
        if age <= age_end / 3:
            return '#77FF80'  # green
        elif age <= age_end / 3 * 2:
            return '#F7FF6D'  # yellow
        else:
            return '#FF638A'  # red

    txt_age = Texts().txt_age

    type_animal = {'cat': 15, 'dog': 20}

    list_images_object = []
    list_move_right_object = []
    list_move_left_object = []
    list_keys = []
    end_age = 0

    for a in range(7):
        random_agr = random.choice(agressive_list)
        image_agr = CircleAvatars().image_agr
        image_agr.foreground_image_src = random_agr

        random_age = random.randint(1, 20)

        for key, _ in type_animal.items():
            list_keys.append(key)
            random_type = random.choice(list_keys)
            end_age = type_animal[random_type]

        color = color_text_picker(random_age, end_age)
        txt_age = copy.deepcopy(txt_age)
        txt_age.color = color
        txt_age.value = random_age

        container_txt_age = Containers().container_txt_age
        container_txt_age.content = txt_age

        icon_stack_right = Stacks().icon_stack_right
        icon_stack_right.controls = [icon_right,
                                     container_txt_age]

        stack_animals = Stacks().stack_animals

        image = copy.deepcopy(image)
        image.src = f'{a + 1}.jpg'
        list_images_object.append(image)

        move_right = copy.deepcopy(move_right)
        move_right.data = a
        list_move_right_object.append(move_right)

        move_left = copy.deepcopy(move_left)
        move_left.data = a
        list_move_left_object.append(move_left)

        random_color = random.choice(colors_gender)

        container_pict_animals = ft.Container(
            ft.Stack([image,
                      move_right,
                      move_left,
                      icon_stack_right,
                      image_agr],
                     width=220,
                     height=220),
            padding=0,
            margin=0,
            bgcolor=ft.Colors.ON_SECONDARY,
            border_radius=12,
            border=ft.border.all(1.5, random_color),
            width=220,
            height=220)

        container_description_animals = (
            ft.Container(
                content=ft.Stack([
                    ft.Container(Texts().txt_name_card(),
                                 width=220,
                                 height=35,
                                 alignment=ft.alignment.center,
                                 ),
                    ft.Container(Texts().txt_description_card(),
                                 width=200,
                                 height=60,
                                 margin=ft.Margin(left=6,
                                                  right=6,
                                                  top=0,
                                                  bottom=3),
                                 alignment=ft.alignment.center,
                                 bottom=1),
                ]),
                bgcolor=ft.Colors.ON_SECONDARY,
                border_radius=12,
                border=ft.border.all(1, random_color),
                width=220,
                height=100,
                bottom=0))

        stack_animals.controls.append(container_pict_animals)
        stack_animals.controls.append(container_description_animals)
        row_elements.controls.append(stack_animals)

    row_cards = Columns().row_cards
    row_cards.controls = [ft.Row(height=22), row_elements]

    content = row_cards

    return content