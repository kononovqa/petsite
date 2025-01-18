import flet as ft

from components.button.icon_button import IconButtons
from components.column.column import Columns
from components.row.row import Rows
from components.text.text import Texts
from config.settings import YANDEX_MAP_URL


def contacts_page(page):
    yandex_map = ft.WebView(
        url=YANDEX_MAP_URL,
        on_web_resource_error=lambda e: print("Page error:", e.data),
        height=500)

    def press_copy(e):
        page.set_clipboard(e.control.data)

    button_copy_address = IconButtons().icon_copy()
    button_copy_address.on_click = press_copy

    button_phone_call = IconButtons().icon_phone()
    button_phone_call.on_click = press_copy

    button_calendar = IconButtons().icon_calendar()
    button_calendar.on_click = press_copy

    txt_main_address = Texts().txt_main_address()
    txt_side_address = Texts().txt_side_address()
    txt_side_phone = Texts().txt_side_phone()
    txt_side_time_work = Texts().txt_side_time_work()
    txt_main_map = Texts().txt_main_map()

    row_txt_main_address = Rows().row_spacing
    row_txt_main_address.controls = [txt_main_address]

    row_txt_side_address = Rows().row_little_spacing
    row_txt_side_address.controls = [button_copy_address, txt_side_address]

    row_txt_side_phone = Rows().row_little_spacing
    row_txt_side_phone.controls = [button_phone_call, txt_side_phone]

    row_txt_side_time_work = Rows().row_little_spacing
    row_txt_side_time_work.controls = [button_calendar, txt_side_time_work]

    row_txt_main_map = Rows().row_spacing
    row_txt_main_map.controls = [txt_main_map]

    row_side_text = ft.Column(controls=[row_txt_side_address,
                                     row_txt_side_phone,
                                     row_txt_side_time_work],
                           height=120,
                           width=340,
                           alignment=ft.MainAxisAlignment.CENTER)

    def resize(width, height):
        if width > 1530:
            row_side_text.width = 1490
            yandex_map.width = 1490
        elif 340 < width < 1530:
            row_side_text.width = width - 40
            yandex_map.width = width - 40
        else:
            row_side_text.width = width
            yandex_map.width = width

    def page_resized(e):
        width_page = int(e.width)
        height_page = int(e.height)
        resize(width=width_page, height=height_page)
        page.update()

    resize(int(page.width), int(page.height))
    #page.on_resized = page_resized

    row_content = Columns().row_cards
    row_content.controls = [row_txt_main_address,
                            row_side_text,
                            row_txt_main_map,
        ft.Row([yandex_map],
               wrap=True,
               alignment=ft.MainAxisAlignment.CENTER)]
    return row_content
