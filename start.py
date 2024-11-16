import os
import urllib3
import uvicorn
import flet as ft
import flet.fastapi as flet_fastapi

from components.button.icon_button import IconButtons
from components.button.text_button import TextButtons
from components.icon.icon import Icons
from components.stack.stack import Stacks
from fastapi_client.apis import api

from pages.router import Router

from components.progress_bar.progress_bar import ProgressBars
from components.container.container import Containers
from components.theme.theme import Theme


async def main(page: ft.Page):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    page.title = "Project N"
    page.horizontal_alignment = "center"
    page.theme_mode = "dark"
    page.theme = Theme().dark_theme
    page.bgcolor = "#1D1A20"
    page.scroll = 'AUTO'

    myRouter = Router(page)
    page.on_route_change = myRouter.route_change

    await page.add_async(myRouter.body)
    await page.go_async('/')

    async def go_main_page(e):
        await page.go_async('/')

    async def go_contacts_page(e):
        await page.go_async('/contacts')

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
        await page.update_async()

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

    def resize():
        width_page = int(page.width)
        horizontal_divider_header.width = width_page - 40
        row_button_switch_theme.width = width_page - 20

    resize()

    async def page_resize(e):
        resize()
        await page.update_async()

    page.on_resize = page_resize
    await page.update_async()


app = flet_fastapi.FastAPI()
app.mount("/api", app=api)
app.mount("/", flet_fastapi.app(main,
                   assets_dir=os.getcwd() + '/assets',
                   web_renderer=ft.WebRenderer.CANVAS_KIT.AUTO))

if __name__ == "__main__":
    uvicorn.run("start:app", log_level="info")
