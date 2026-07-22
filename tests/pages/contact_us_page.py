from playwright.sync_api import Page


class ContactUsPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.wait_for_load_state("load")
        self.get_in_touch_heading = page.get_by_text("GET IN TOUCH")
        self.name_textbox = page.get_by_placeholder("Name")
        self.email_textbox = page.get_by_placeholder("Email", exact=True)
        self.subject_textbox = page.get_by_placeholder("Subject")
        self.message_textbox = page.get_by_placeholder("Your Message Here")
        self.file_upload_input = page.locator('input[type="file"]')
        self.submit_button = page.locator("input[data-qa='submit-button']")
        self.success_message = page.locator("#contact-page").get_by_text(
            "Success! Your details have been submitted successfully."
        )

    def fill_customer_information(
        self, name: str, email: str, subject: str, message: str, file_path: str
    ):
        self.name_textbox.fill(name)
        self.email_textbox.fill(email)
        self.subject_textbox.fill(subject)
        self.message_textbox.fill(message)

        # upload a file
        self.file_upload_input.set_input_files(file_path)

    def click_submit(self):
        self.submit_button.click()
