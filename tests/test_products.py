from playwright.sync_api import expect, Page

PRODUCT_CARDS = ".features_items .product-image-wrapper"


def test_verify_all_products_and_product_detail_page(page: Page, home):
    # navigate to the products page
    products_page = home.header.go_to_products_page()

    # assert that the products page is visible successfully
    expect(page).to_have_url("/products")
    expect(page.get_by_role("heading", name="All Products")).to_be_visible()

    products = page.locator(PRODUCT_CARDS)
    expect(products.first).to_be_visible()

    # open the first product detail page
    products_page.view_product_details_of_nth_product(0)

    # assert that the product detail is visible successfully
    expect(page).to_have_url("/product_details/1")
    product_information = page.locator(".product-information")
    expect(product_information.get_by_role("heading", name="Blue Top")).to_be_visible()
    expect(product_information.get_by_text("Category: Women")).to_be_visible()
    expect(product_information.get_by_text("Rs. 500")).to_be_visible()
    expect(product_information.get_by_text("Availability:")).to_be_visible()
    expect(product_information.get_by_text("Condition:")).to_be_visible()
    expect(product_information.get_by_text("Brand:")).to_be_visible()


def test_search_product(page: Page, home):
    search_term = "top"

    # open the products page
    products_page = home.header.go_to_products_page()
    expect(page).to_have_url("/products")

    # search for a product
    products_page.search_products(search_term)

    # assert that the searched products page is visible successfully
    expect(page.get_by_role("heading", name="Searched Products")).to_be_visible()
    products = page.locator(PRODUCT_CARDS)
    expect(products.first).to_be_visible()
    total = products.count()
    relevant = products.filter(has_text=search_term).count()
    assert (
        total == relevant
    ), f"Expected all {total} products to contain '{search_term}', but only {relevant} contain it in title name."
