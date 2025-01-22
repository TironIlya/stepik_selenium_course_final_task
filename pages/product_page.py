from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    # Локаторы
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

    def add_product_to_basket(self):
        # Нажимаем на кнопку "Добавить в корзину"
        add_to_basket_button = self.browser.find_element(*self.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_not_be_success_message(self):
        # Проверяем, что сообщение об успехе не отображается
        assert self.is_not_element_present(*self.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        # Проверяем, что сообщение об успехе исчезает
        assert self.is_disappeared(*self.SUCCESS_MESSAGE), \
            "Success message did not disappear, but it should"
        
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented"
