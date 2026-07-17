from playwright.sync_api import Page


class Footer:
    def __init__(self, page: Page):
        self.page = page

    def scroll_to_footer(self):
        self.page.locator("#footer").scroll_into_view_if_needed()

    def subscribe(self, email: str):
        self.page.get_by_role("textbox", name="Your email address").fill(email)
        self.page.locator("#subscribe").click()
