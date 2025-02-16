import pytest
import time
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

product_page_link1 = (
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
)
product_page_link2 = (
    "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
)


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://selenium1py.pythonanywhere.com/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "!1aA"
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, product_page_link1)
        page.open()
        page.add_product_to_basket()
        page.should_be_right_product_title_in_success_message()
        page.should_be_right_price_in_success_message()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, product_page_link1)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, product_page_link2)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_message_about_empty_basket()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_page_link2)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
@pytest.mark.parametrize(
    "offer_number",
    [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        pytest.param("7", marks=pytest.mark.xfail),
        "8",
        "9",
    ],
)
def test_guest_can_add_product_to_basket(browser, offer_number):
    link = f"{product_page_link1}?promo=offer{offer_number}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_right_product_title_in_success_message()
    page.should_be_right_price_in_success_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_page_link1)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_page_link1)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_page_link1)
    page.open()
    page.add_product_to_basket()
    page.success_message_disappears()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, product_page_link2)
    page.open()
    page.should_be_login_link()
