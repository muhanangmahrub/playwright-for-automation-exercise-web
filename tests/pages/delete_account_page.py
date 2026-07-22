from playwright.sync_api import Page


class DeleteAccountPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.wait_for_load_state("load")
        self.account_deleted_heading = page.get_by_text("Account Deleted!")
        self.continue_link = page.get_by_role("link", name="Continue")

    def continue_after_account_deletion(self):
        self.continue_link.click()
