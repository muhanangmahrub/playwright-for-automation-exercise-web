from playwright.sync_api import Page


class SignupDetailPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.wait_for_load_state("load")
        self.account_information_heading = page.get_by_text("Enter Account Information")
        self.account_created_heading = page.get_by_text("Account Created!")
        self.mr_radio = page.get_by_role("radio", name="Mr.")
        self.mrs_radio = page.get_by_role("radio", name="Mrs.")
        self.password_textbox = page.get_by_role("textbox", name="Password *")
        self.day_dropdown = page.locator("#days")
        self.month_dropdown = page.locator("#months")
        self.year_dropdown = page.locator("#years")
        self.newsletter_checkbox = page.get_by_role(
            "checkbox", name="Sign up for our newsletter!"
        )
        self.special_offers_checkbox = page.get_by_role(
            "checkbox", name="Receive special offers from our partners!"
        )
        self.first_name_textbox = page.get_by_role("textbox", name="First name *")
        self.last_name_textbox = page.get_by_role("textbox", name="Last name *")
        self.company_textbox = page.get_by_role("textbox", name="Company", exact=True)
        self.address_textbox = page.get_by_role(
            "textbox", name="Address * (Street address, P."
        )
        self.address_2_textbox = page.get_by_role("textbox", name="Address 2")
        self.country_dropdown = page.get_by_label("Country *")
        self.state_textbox = page.get_by_role("textbox", name="State *")
        self.city_textbox = page.get_by_role("textbox", name="City * Zipcode *")
        self.zipcode_textbox = page.locator("#zipcode")
        self.mobile_number_textbox = page.get_by_role("textbox", name="Mobile Number *")
        self.create_account_button = page.get_by_role("button", name="Create Account")
        self.continue_link = page.get_by_role("link", name="Continue")

    def fill_account_information(
        self,
        title: str,
        password: str,
        day: str,
        month: str,
        year: str,
        newsletter: bool = False,
        offers: bool = False,
        first_name: str = "Febri",
        last_name: str = "Haryono",
        company: str = "Nawadata",
        address1: str = "Baciro",
        address2: str = "Gondokusuman",
        country: str = "Australia",
        state: str = "Oakland",
        city: str = "Oklahoma",
        zipcode: str = "12345",
        mobile_number: str = "123456789",
    ):
        if title.lower() == "mr":
            self.mr_radio.check()
        elif title.lower() == "mrs":
            self.mrs_radio.check()
        else:
            raise ValueError("Invalid title. Please choose 'Mr' or 'Mrs'.")

        self.password_textbox.fill(password)
        self.day_dropdown.select_option(day)
        self.month_dropdown.select_option(month)
        self.year_dropdown.select_option(year)

        if newsletter:
            self.newsletter_checkbox.check()

        if offers:
            self.special_offers_checkbox.check()
        self.first_name_textbox.fill(first_name)
        self.last_name_textbox.fill(last_name)
        self.company_textbox.fill(company)
        self.address_textbox.fill(address1)
        self.address_2_textbox.fill(address2)
        self.country_dropdown.select_option(country)
        self.state_textbox.fill(state)
        self.city_textbox.fill(city)
        self.zipcode_textbox.fill(zipcode)
        self.mobile_number_textbox.fill(mobile_number)
        self.create_account_button.click()

    def continue_after_account_creation(self):
        self.continue_link.click()
