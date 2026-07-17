from playwright.sync_api import expect, Page


def test_add_products_in_cart(page: Page, home):
    # open the homepage and navigate to the products page
    products_page = home.header.go_to_products_page()
    expect(page).to_have_url("/products")

    # add to cart the first product
    products_page.add_nth_product_to_cart(0)
    products_page.continue_shopping()

    # add to cart the second product
    products_page.add_nth_product_to_cart(1)
    products_page.view_cart()

    # assert that the cart page is visible and the products are added to the cart
    expect(page).to_have_url("/view_cart")
    expect(page.get_by_text("Blue Top")).to_be_visible()
    expect(page.get_by_text("Men Tshirt")).to_be_visible()
    expect(
        page.locator("#product-1").locator(".cart_price").get_by_text("Rs. 500")
    ).to_be_visible()
    expect(
        page.locator("#product-2").locator(".cart_price").get_by_text("Rs. 400")
    ).to_be_visible()


def test_verify_product_quantity_in_cart(page: Page, home):
    # open the homepage and navigate to the products page
    products_page = home.header.go_to_products_page()
    expect(page).to_have_url("/products")

    # view product details of the any product
    product_detail_page = products_page.view_product_details_of_nth_product(0)
    expect(page).to_have_url("/product_details/1")

    # increase quantity to 4 and add to cart
    product_detail_page.increase_quantity(4)
    product_detail_page.add_to_cart()
    product_detail_page.view_cart()

    # assert that product is displayed in cart page with exact quantity
    expect(page).to_have_url("/view_cart")
    first_product = page.locator("#product-1")
    expect(
        first_product.locator(".cart_description").get_by_text("Blue Top")
    ).to_be_visible()
    expect(first_product.locator(".cart_price").get_by_text("Rs. 500")).to_be_visible()
    expect(first_product.locator(".cart_quantity").get_by_text("4")).to_be_visible()
    expect(first_product.locator(".cart_total").get_by_text("Rs. 2000")).to_be_visible()
