from playwright.sync_api import expect, Page

PRODUCT_CARDS = ".features_items .product-image-wrapper"


def test_verify_all_products_and_product_detail_page(page: Page):
    # open the homepage
    page.goto("/")
    expect(page).to_have_title("Automation Exercise")

    # navigate to the products page
    page.locator(".shop-menu").get_by_role("link", name="Products").click()

    # assert that the products page is visible successfully
    expect(page).to_have_url("/products")
    expect(page.get_by_role("heading", name="All Products")).to_be_visible()

    products = page.locator(PRODUCT_CARDS)
    expect(products.first).to_be_visible()

    # open the first product detail page
    products.first.get_by_role("link", name="View Product").click()

    # assert that the product detail is visible successfully
    expect(page).to_have_url("/product_details/1")
    product_information = page.locator(".product-information")
    expect(product_information.get_by_role("heading", name="Blue Top")).to_be_visible()
    expect(product_information.get_by_text("Category: Women")).to_be_visible()
    expect(product_information.get_by_text("Rs. 500")).to_be_visible()
    expect(product_information.get_by_text("Availability:")).to_be_visible()
    expect(product_information.get_by_text("Condition:")).to_be_visible()
    expect(product_information.get_by_text("Brand:")).to_be_visible()


def test_search_product(page: Page):
    search_term = "top"

    # open the products page
    page.goto("/")
    expect(page).to_have_title("Automation Exercise")
    page.get_by_role("link", name="Products").click()
    expect(page).to_have_url("/products")

    # search for a product
    page.get_by_role("textbox", name="Search Product").fill(search_term)
    page.locator("#submit_search").click()

    # assert that the searched products page is visible successfully
    expect(page.get_by_role("heading", name="Searched Products")).to_be_visible()
    products = page.locator(PRODUCT_CARDS)
    expect(products.first).to_be_visible()
    total = products.count()
    relevant = products.filter(has_text=search_term).count()
    assert (
        total == relevant
    ), f"Expected all {total} products to contain '{search_term}', but only {relevant} contain it in title name."
