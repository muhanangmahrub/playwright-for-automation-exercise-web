import pytest

AD_HOSTS = (
    "googlesyndication.com",
    "doubleclick.net",
    "adservice.google.com",
    "googletagmanager.com",
    "googletagservices.com",
)


@pytest.fixture(autouse=True)
def block_ads(page):
    page.route(
        "**/*",
        lambda route: (
            route.abort()
            if any(host in route.request.url for host in AD_HOSTS)
            else route.continue_()
        ),
    )


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "viewport": {"width": 1920, "height": 1080}}
