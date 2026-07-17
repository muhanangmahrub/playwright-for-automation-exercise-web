from playwright.sync_api import Page


class SignupDetailPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.wait_for_load_state("load")

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
            self.page.get_by_role("radio", name="Mr.").check()
        elif title.lower() == "mrs":
            self.page.get_by_role("radio", name="Mrs.").check()
        else:
            raise ValueError("Invalid title. Please choose 'Mr' or 'Mrs'.")

        self.page.get_by_role("textbox", name="Password *").fill(password)
        self.page.locator("#days").select_option(day)
        self.page.locator("#months").select_option(month)
        self.page.locator("#years").select_option(year)

        if newsletter:
            self.page.get_by_role(
                "checkbox", name="Sign up for our newsletter!"
            ).check()

        if offers:
            self.page.get_by_role(
                "checkbox", name="Receive special offers from our partners!"
            ).check()
        self.page.get_by_role("textbox", name="First name *").fill(first_name)
        self.page.get_by_role("textbox", name="Last name *").fill(last_name)
        self.page.get_by_role("textbox", name="Company", exact=True).fill(company)
        self.page.get_by_role("textbox", name="Address * (Street address, P.").fill(
            address1
        )
        self.page.get_by_role("textbox", name="Address 2").fill(address2)
        self.page.get_by_label("Country *").select_option(country)
        self.page.get_by_role("textbox", name="State *").fill(state)
        self.page.get_by_role("textbox", name="City * Zipcode *").fill(city)
        self.page.locator("#zipcode").fill(zipcode)
        self.page.get_by_role("textbox", name="Mobile Number *").fill(mobile_number)
        self.page.get_by_role("button", name="Create Account").click()

    def continue_after_account_creation(self):
        self.page.get_by_role("link", name="Continue").click()
