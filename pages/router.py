import flet as ft

from pages.contacts_page import contacts_page
from pages.help_page import help_page
from pages.main_page import main_page
from pages.pets_page import pets_page


class Router:

    def __init__(self, page):
        self.page = page
        self.ft = ft
        self.routes = {
            "/": main_page(page),
            "/contacts": contacts_page(page),
            '/pets': pets_page(page),
            '/help': help_page(page)
        }
        self.body = ft.Container(content=self.routes['/'])

    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()