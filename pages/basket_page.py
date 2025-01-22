from .base_page import BasePage
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(By.CSS_SELECTOR, ".basket-items"), "Basket is not empty!"

    def should_be_empty_basket_text(self):
        empty_text = self.browser.find_element(By.CSS_SELECTOR, "#content_inner").text
        assert "Ваша корзина пуста" in empty_text, f"Expected 'Ваша корзина пуста' in '{empty_text}'"
  