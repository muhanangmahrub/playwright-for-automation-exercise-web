from playwright.sync_api import expect, Page

def test_add_products_in_cart(page: Page):
    # open the homepage and navigate to the products page
    page.goto("/")
    expect(page).to_have_title("Automation Exercise")
    page.locator(".shop-menu").get_by_role("link", name="Products").click()
    expect(page).to_have_url("/products")

    # add to cart the first product
    products = page.locator(".features_items .product-image-wrapper")
    products.first.get_by_text("Add to cart").nth(0).click()
    page.get_by_role("button", name="Continue Shopping").click()

    # add to cart the second product
    products.nth(1).get_by_text("Add to cart").nth(0).click()
    page.get_by_role("link", name="View Cart").click()

    # assert that the cart page is visible and the products are added to the cart
    expect(page).to_have_url("/view_cart")
    expect(page.get_by_text("Blue Top")).to_be_visible()
    expect(page.get_by_text("Men Tshirt")).to_be_visible()
    expect(page.get_by_text("Rs. 500").nth(0)).to_be_visible()
    expect(page.get_by_text("Rs. 400").nth(0)).to_be_visible()