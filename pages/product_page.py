from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import math


class ProductPage:
    # Локаторы
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_TITLE = (By.TAG_NAME, "h1")  # Заголовок товара
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")  # Цена товара
    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR,
        ".alertinner strong",
    )  # Сообщение об успешном добавлении
    BASKET_TOTAL_MESSAGE = (
        By.CSS_SELECTOR,
        ".alert-info .alertinner p",
    )  # Информация о стоимости корзины

    def __init__(self, browser):
        self.browser = browser

    def add_product_to_basket(self):
        # Нажимаем на кнопку "Добавить в корзину"
        add_to_basket_button = self.browser.find_element(*self.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def solve_quiz_and_get_code(self):
        # Решаем математическую задачу и получаем код
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs(12 * math.sin(float(x)))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except Exception as e:
            print(f"No second alert presented: {e}")

    def get_product_title(self):
        # Получаем заголовок товара
        return self.browser.find_element(*self.PRODUCT_TITLE).text

    def get_product_price(self):
        # Получаем цену товара
        return self.browser.find_element(*self.PRODUCT_PRICE).text

    def get_product_name_from_message(self):
        # Получаем название товара из сообщения о добавлении в корзину
        return self.browser.find_element(*self.SUCCESS_MESSAGE).text

    def get_basket_total(self):
        # Получаем информацию о стоимости корзины
        return self.browser.find_element(*self.BASKET_TOTAL_MESSAGE).text
