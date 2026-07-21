import pytest
import random
import string
import datetime
import os
from tests.pages.home_page import HomePage
from faker import Faker
from dotenv import load_dotenv

load_dotenv()

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


@pytest.fixture(scope="session")
def faker():
    return Faker("id_ID")


@pytest.fixture(scope="session")
def credentials():
    return {
        "email": os.environ["EMAIL_LOGIN"],
        "password": os.environ["PASSWORD_LOGIN"],
        "existing_name": os.environ["EXISTING_NAME"],
        "existing_email": os.environ["EXISTING_EMAIL"],
    }


@pytest.fixture
def home(page):
    home = HomePage(page)
    home.open()
    return home


@pytest.fixture
def dummy_email():
    domain = "demo.org"
    name = "".join(random.choices(string.ascii_lowercase, k=12))
    date_time = datetime.datetime.now()
    date = date_time.strftime("%Y%m%d%H%M%S")
    return f"{name}{date}@{domain}"


@pytest.fixture
def user_data(faker):
    next_year = datetime.datetime.now().year + 2
    return {
        "name": str(faker.name()),
        "card_number": str(faker.credit_card_number()),
        "cvc": str(faker.credit_card_security_code()),
        "month": str(faker.month()),
        "year": str(next_year),
    }


@pytest.fixture
def cleanup_account(home):
    yield
    if home.header.is_logged_in():
        home.header.delete_account()
