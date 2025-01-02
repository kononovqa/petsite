import os
import urllib3
import uvicorn

import flet as ft
import flet.fastapi as flet_fastapi

from fastapi_client.apis import api
from pages.router import Router

from components.theme.theme import Theme


async def main(page: ft.Page):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    page.title = "Project N"
    page.horizontal_alignment = "center"
    page.theme_mode = "dark"
    page.bgcolor = "#1D1A20"
    page.scroll = 'AUTO'
    myRouter = Router(page)
    page.on_route_change = myRouter.route_change

    page.fonts = {
        "NotoSansBold": "fonts/NotoSans-Bold.ttf",
        "NotoSansRegular": "fonts/NotoSans-Regular.ttf",
    }

    page.dark_theme = Theme().dark_theme
    page.theme = Theme().light_theme

    page.add(myRouter.body)
    page.go('/')


app = flet_fastapi.FastAPI()

app.mount("/api", app=flet_fastapi.app(api))
app.mount("/", app=flet_fastapi.app(main,
                   assets_dir=os.getcwd() + '/assets'))


if __name__ == "__main__":
    uvicorn.run("start:app")
