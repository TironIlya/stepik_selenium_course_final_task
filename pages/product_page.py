from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        # Нажимаем на кнопку "Добавить в корзину"
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_not_be_success_message(self):
        # Проверяем, что сообщение об успехе не отображается
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        # Проверяем, что сообщение об успехе исчезает
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappear, but it should"

    def should_be_success_message(self):
        # Проверяем, что сообщение об успехе отображается
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented"

    def go_to_login_page(self):
        # Переход на страницу логина
        login_link = self.browser.find_element(*ProductPageLocators.LOGIN_LINK)
        login_link.click()
