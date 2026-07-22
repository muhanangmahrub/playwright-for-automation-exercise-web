from playwright.sync_api import Page


class TestCasesPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.wait_for_load_state("load")
        self.description_message = page.get_by_text(
            "Below is the list of test Cases for you to practice the Automation"
        )
