from playwright.sync_api import Page


class ConfirmPage:
    def __init__(self, page: Page):
        self.page = page

    def click_continue(self):
        self.page.get_by_role("link", name="Continue").click()
