import flet as ft


class Icons:
    def __init__(self):
        self.icon_dark_theme = ft.icons.DARK_MODE
        self.icon_light_theme = ft.icons.LIGHT_MODE
        self.icon_move_right = ft.Icon(name=ft.Icons.CHEVRON_RIGHT_OUTLINED
                                       , color=ft.Colors.TRANSPARENT)
        self.icon_move_left = ft.Icon(name=ft.Icons.CHEVRON_LEFT_OUTLINED
                                      , color=ft.Colors.TRANSPARENT)
        self.icon_copy = ft.icons.COPY
        self.icon_phone = ft.icons.LOCAL_PHONE
        self.icon_calendar = ft.icons.CALENDAR_MONTH
