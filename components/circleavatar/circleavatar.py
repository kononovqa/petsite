import flet as ft


class CircleAvatars:
    def __init__(self):
        self.icon_right = ft.CircleAvatar(foreground_image_src='grey.png')

        self.image_agr = ft.CircleAvatar(foreground_image_src='',
                                    bottom=0,
                                    left=0,
                                    width=30,
                                    height=30,
                                    offset=(0.18, -0.18))
