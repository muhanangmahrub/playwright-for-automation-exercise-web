from tests.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def open(self):
        self.page.goto("/", wait_until="domcontentloaded")
