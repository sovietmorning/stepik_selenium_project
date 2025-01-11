from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group > a.btn")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_EMAIL = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[value='Log In']")
    LOGIN_FORGOT_PW_LINK = (By.CSS_SELECTOR, "#login_form a")

    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_REPEAT_PASSWORD = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[value='Register']")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_TITLE = (By.TAG_NAME, "h1")
    PRODUCT_TITLE_IN_SUCCESS_MESSAGE = (
        By.CSS_SELECTOR,
        "#messages .alert-success:first-child strong",
    )
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:first-child")


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    ITEMS_IN_BASKET_FORM = (By.ID, "basket_formset")
    PROCEED_TO_CHECKOUT_BUTTON = (By.CSS_SELECTOR, "#content_inner .btn-block")
