from playwright.sync_api import expect

def test_verify_all_products_and_product_detail_page(page):
    page.goto("/")
    expect(page).to_have_title("Automation Exercise")

    page.locator(".shop-menu").get_by_role("link", name="Products").click()
    page.wait_for_load_state("load")
    expect(page).to_have_url("/products")
    expect(page.get_by_role("heading", name="All Products")).to_be_visible()

    products = page.locator(".features_items .product-image-wrapper")
    expect(products.first).to_be_visible()

    products.first.get_by_role('link', name="View Product").click()
    expect(page).to_have_url("/product_details/1")

    product_information = page.locator(".product-information")

    expect(product_information.get_by_role("heading", name="Blue Top")).to_be_visible()
    expect(product_information.get_by_text("Category: Women")).to_be_visible()
    expect(product_information.get_by_text("Rs. 500")).to_be_visible()
    expect(product_information.get_by_text("In Stock")).to_be_visible()
    expect(product_information.get_by_text("Condition: New")).to_be_visible()
    expect(product_information.get_by_text("Brand: Polo")).to_be_visible()