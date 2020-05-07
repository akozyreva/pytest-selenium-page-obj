from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REG_FORM = (By.CSS_SELECTOR, "form#register_form")


class ProductPageLocators():
    BASKET_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")