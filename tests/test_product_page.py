import pytest
from pages.product_page import ProductPage


@pytest.mark.parametrize("link", ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    # Открываем страницу товара
    page = ProductPage(browser, link)
    page.open()

    # Добавляем товар в корзину
    page.add_product_to_basket()

    # Проверяем, что нет сообщения об успехе
    page.should_not_be_success_message()

@pytest.mark.parametrize("link", ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message(browser, link):
    # Открываем страницу товара
    page = ProductPage(browser, link)
    page.open()

    # Проверяем, что нет сообщения об успехе
    page.should_not_be_success_message()

@pytest.mark.parametrize("link", ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    # Открываем страницу товара
    page = ProductPage(browser, link)
    page.open()

    # Добавляем товар в корзину
    page.add_product_to_basket()

    # Проверяем, что сообщение об успехе исчезает
    page.should_disappear_success_message()
