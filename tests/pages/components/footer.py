from playwright.sync_api import Page


class Footer:
    def __init__(self, page: Page):
        self.page = page
        self.footer_section = page.locator("#footer")
        self.subscription_heading = page.get_by_role("heading", name="Subscription")
        self.email_textbox = page.get_by_role("textbox", name="Your email address")
        self.subscribe_button = page.locator("#subscribe")
        self.subscription_success_message = page.get_by_text(
            "You have been successfully"
        )

    def scroll_to_footer(self):
        self.footer_section.scroll_into_view_if_needed()

    def subscribe(self, email: str):
        self.email_textbox.fill(email)
        self.subscribe_button.click()
