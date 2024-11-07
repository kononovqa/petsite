import os
import urllib3
import uvicorn
import flet as ft
import flet.fastapi as flet_fastapi

from components.icon.icon import Icons
from fastapi_client.apis import api

from pages.router import Router

from components.progress_bar.progress_bar import ProgressBars
from components.container.container import Containers
from components.text.text import Texts
from components.button.elevated_button import ElevatedButtons


async def main(page: ft.Page):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    page.title = "Project N"
    page.horizontal_alignment = "center"
    page.theme_mode = "dark"
    page.scroll = 'AUTO'

    myRouter = Router(page)
    page.on_route_change = myRouter.route_change
    await page.add_async(myRouter.body)
    await page.go_async('/')

    async def go_main_page(e):
        await page.go_async('/')

    async def change_theme(e):
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        button_switch_theme.content = Icons().icon_switch_theme_to_light if page.theme_mode == "dark" else Icons().icon_switch_theme_to_dark
        await page.update_async()

    button_switch_theme = ElevatedButtons().elevated_button_switch_mode
    button_switch_theme.content = Icons().icon_switch_theme_to_light
    button_switch_theme.on_click = change_theme

    button_main = ft.TextButton(
        content=Texts().txt_header_main(),
        on_click=go_main_page)

    button_contacts = ft.TextButton(
        content=Texts().txt_header_contacts(),
        on_click=go_main_page)

    horizontal_divider_header = Containers().horizontal_divider

    row_vertical_divider_header = ft.Row(
        [horizontal_divider_header],
        height=16,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.alignment.bottom_center)

    row_header = ft.Row(
        [button_main, ProgressBars().vertical_divider, button_contacts, ProgressBars().vertical_divider,
         button_switch_theme],
        alignment=ft.MainAxisAlignment.CENTER)

    page.appbar = ft.AppBar(
        title=ft.Column([
            row_header,
            row_vertical_divider_header
        ]),
        toolbar_height=100)

    def resize():
        width_page = int(page.width)
        horizontal_divider_header.width = width_page - 40

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
