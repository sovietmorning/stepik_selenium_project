from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.ITEMS_IN_BASKET_FORM
        ), "Some items are in basket, but should not be"

    def should_be_message_about_empty_basket(self):
        empty_basket_message = self.browser.find_element(
            *BasketPageLocators.EMPTY_BASKET_MESSAGE
        )
        print(f"Basket message is: '{empty_basket_message.text}'")
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_BASKET_MESSAGE
        ), "Message about empty basket is not presented"
