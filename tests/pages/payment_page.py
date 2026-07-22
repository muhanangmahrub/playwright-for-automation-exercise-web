from playwright.sync_api import Page
from tests.pages.confirm_page import ConfirmPage


class PaymentPage:
    def __init__(self, page: Page):
        self.page = page
        self.name_on_card_textbox = page.locator('input[name="name_on_card"]')
        self.card_number_textbox = page.locator('input[name="card_number"]')
        self.cvc_textbox = page.get_by_role("textbox", name="ex.")
        self.expiry_month_textbox = page.get_by_role("textbox", name="MM")
        self.expiry_year_textbox = page.get_by_role("textbox", name="YYYY")
        self.pay_and_confirm_button = page.get_by_role(
            "button", name="Pay and Confirm Order"
        )

    def fill_payment_details(
        self, name: str, card_number: str, cvc: str, month: str, year: str
    ):
        self.name_on_card_textbox.fill(name)
        self.card_number_textbox.fill(card_number)
        self.cvc_textbox.fill(cvc)
        self.expiry_month_textbox.fill(month)
        self.expiry_year_textbox.fill(year)
        self.pay_and_confirm_button.click()
        return ConfirmPage(self.page)
