import pytest
from selenium import webdriver
from pages.product_page import ProductPage


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.parametrize(
    "link",
    [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        pytest.param(
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
            marks=pytest.mark.xfail,
        ),
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
    ],
)
def test_guest_can_add_product_to_basket(browser, link):
    # Открываем ссылку
    browser.get(link)

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
