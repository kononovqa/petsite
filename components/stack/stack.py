import flet as ft


class Stacks:
    def __init__(self):
        self.stack_def = ft.Stack()

        self.icon_stack_right = ft.Stack(
                                    right=1,
                                    bottom=1,
                                    width=30,
                                    height=30,
                                    offset=(-0.18, -0.18),
                                    )

        self.stack_animals = ft.Stack(width=220, height=332)


    def stack_app_bar(self):
        return self.stack_def