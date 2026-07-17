from tests.pages.components.header import Header
from playwright.sync_api import Page
from tests.pages.components.footer import Footer


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.header = Header(page)
        self.footer = Footer(page)
