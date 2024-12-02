import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Обработчик командной строки для параметра language
def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default="en", help="Choose language"
    )

# Фикстура для браузера
@pytest.fixture
def browser(request):
    language = request.config.getoption("--language")
    
    # Настройка опций браузера
    options = Options()
    options.add_argument(f"--lang={language}")  # Устанавливаем язык браузера
    
    # Запуск браузера
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
