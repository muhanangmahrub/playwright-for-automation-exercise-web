from playwright.sync_api import Page, expect
from tests.pages.address_page import AddressPage


def complete_payment(
    address_page: AddressPage,
    name: str,
    card_number: str,
    cvc: str,
    month: str,
    year: str,
):
    payment_page = address_page.place_order()
    return payment_page.fill_payment_details(name, card_number, cvc, month, year)


def assert_order_placed(page: Page):
    expect(page.get_by_text("Order Placed!")).to_be_visible()
    expect(page.get_by_text("Congratulations! Your order")).to_be_visible()
    expect(page.get_by_role("link", name="Download Invoice")).to_be_visible()


def test_place_order_register_while_checkout(
    page: Page, home, dummy_email, user_data, cleanup_account
):
    products_page = home.header.go_to_products_page()
    products_page.products.add_nth_product_to_cart(0)

    cart_page = products_page.products.view_cart()
    expect(page).to_have_url("/view_cart")
    cart_page.proceed_to_checkout_as_guest()

    login_signup_page = cart_page.register_or_login()
    expect(page).to_have_url("/login")
    signup_detail_page = login_signup_page.signup(user_data["name"], dummy_email)
    expect(page).to_have_url("/signup")
    signup_detail_page.fill_account_information(
        title="Mr",
        password="testing",
        day="11",
        month="7",
        year="2004",
        newsletter=True,
        offers=True,
    )
    signup_detail_page.continue_after_account_creation()

    cart_page = home.header.go_to_cart_page()
    expect(page).to_have_url("/view_cart")
    address_page = cart_page.proceed_to_checkout()
    expect(page.get_by_role("heading", name="Address Details")).to_be_visible()
    expect(page.get_by_role("heading", name="Review Your Order")).to_be_visible()

    confirm_page = complete_payment(
        address_page,
        user_data["name"],
        user_data["card_number"],
        user_data["cvc"],
        user_data["month"],
        user_data["year"],
    )
    assert_order_placed(page)
    confirm_page.click_continue()


def test_place_order_register_before_checkout(
    page: Page, home, user_data, dummy_email, cleanup_account
):
    # open the homepage and navigate to the signup page
    login_signup_page = home.header.go_to_login_signup_page()

    # fill out the signup form and submit it
    signup_detail_page = login_signup_page.signup(user_data["name"], dummy_email)

    # assert that signup details page is visible
    expect(page.get_by_text("Enter Account Information")).to_be_visible()

    # fill out the account information form and submit it
    signup_detail_page.fill_account_information(
        title="Mr",
        password="testing",
        day="11",
        month="7",
        year="2004",
        newsletter=True,
        offers=True,
    )

    # assert that account created page is visible
    expect(page.get_by_text("Account Created!")).to_be_visible()
    signup_detail_page.continue_after_account_creation()
    expect(page.get_by_text("Logged in")).to_be_visible()

    products_page = home.header.go_to_products_page()
    products_page.products.add_nth_product_to_cart(0)

    cart_page = products_page.products.view_cart()
    expect(page).to_have_url("/view_cart")
    address_page = cart_page.proceed_to_checkout()
    expect(page.get_by_role("heading", name="Address Details")).to_be_visible()
    expect(page.get_by_role("heading", name="Review Your Order")).to_be_visible()

    confirm_page = complete_payment(
        address_page,
        user_data["name"],
        user_data["card_number"],
        user_data["cvc"],
        user_data["month"],
        user_data["year"],
    )
    assert_order_placed(page)
    confirm_page.click_continue()


def test_place_order_login_before_checkout(page: Page, credentials, home, user_data):
    # open the homepage and navigate to the login page
    login_signup_page = home.header.go_to_login_signup_page()

    # fill out the login form and submit it
    login_signup_page.login(credentials["email"], credentials["password"])

    # assert that user is logged in successfully
    expect(page.get_by_text("Logged in as")).to_be_visible()
    products_page = home.header.go_to_products_page()
    products_page.products.add_nth_product_to_cart(0)

    cart_page = products_page.products.view_cart()
    expect(page).to_have_url("/view_cart")
    address_page = cart_page.proceed_to_checkout()
    expect(page.get_by_role("heading", name="Address Details")).to_be_visible()
    expect(page.get_by_role("heading", name="Review Your Order")).to_be_visible()

    confirm_page = complete_payment(
        address_page,
        user_data["name"],
        user_data["card_number"],
        user_data["cvc"],
        user_data["month"],
        user_data["year"],
    )
    assert_order_placed(page)
    confirm_page.click_continue()

    expect(page.get_by_role("link", name="Logout")).to_be_visible()
