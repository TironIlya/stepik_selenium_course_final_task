import pytest
from selenium import webdriver
from pages.product_page import ProductPage


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.get(
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    )
    yield driver
    driver.quit()


def test_guest_can_add_product_to_basket(browser):
    # Создаем объект страницы товара
    page = ProductPage(browser)

    # Получаем заголовок товара и его цену
    product_title = page.get_product_title()
    product_price = page.get_product_price()

    # Добавляем товар в корзину
    page.add_product_to_basket()

    # Решаем задачу и получаем проверочный код
    page.solve_quiz_and_get_code()

    # Получаем имя товара из сообщения о добавлении в корзину
    product_name_in_message = page.get_product_name_from_message()

    # Проверяем, что название товара в сообщении совпадает с заголовком товара
    assert (
        product_name_in_message == product_title
    ), f"Expected product name '{product_title}', but got '{product_name_in_message}'"

    # Проверяем, что стоимость корзины соответствует цене товара
    basket_total = page.get_basket_total()
    assert (
        product_price in basket_total
    ), f"Expected basket total to contain '{product_price}', but got '{basket_total}'"
