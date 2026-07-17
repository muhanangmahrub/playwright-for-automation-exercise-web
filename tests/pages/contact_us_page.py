from playwright.sync_api import Page


class ContactUsPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.wait_for_load_state("load")

    def fill_customer_information(
        self, name: str, email: str, subject: str, message: str, file_path: str
    ):
        self.page.get_by_placeholder("Name").fill(name)
        self.page.get_by_placeholder("Email", exact=True).fill(email)
        self.page.get_by_placeholder("Subject").fill(subject)
        self.page.get_by_placeholder("Your Message Here").fill(message)

        # upload a file
        self.page.locator('input[type="file"]').set_input_files(file_path)

    def click_submit(self):
        self.page.locator("input[data-qa='submit-button']").click()
