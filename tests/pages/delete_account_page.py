from playwright.sync_api import Page


class DeleteAccountPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.wait_for_load_state("load")

    def continue_after_account_deletion(self):
        self.page.get_by_role("link", name="Continue").click()
