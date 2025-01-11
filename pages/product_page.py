from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button.click()

    def should_be_right_product_title_in_success_message(self):
        title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE)
        title_in_message = self.browser.find_element(
            *ProductPageLocators.PRODUCT_TITLE_IN_SUCCESS_MESSAGE
        )
        print(
            f"The product title is: '{title.text}', the title in message is: '{title_in_message.text}'"
        )
        assert (
            title.text == title_in_message.text
        ), "The title in success message differs from the product title"

    def should_be_right_price_in_success_message(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        price_in_message = self.browser.find_element(
            *ProductPageLocators.PRICE_BASKET_TOTAL
        )
        print(
            f"The product price is: '{price.text}', the price in message is: '{price_in_message.text}'"
        )
        assert (
            price.text == price_in_message.text
        ), "The price in success message differs from the product price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is presented, but should not be"

    def success_message_disappears(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message hasn't disappeared"
