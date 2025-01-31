from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, f"Expected 'login' to be in URL, but got {current_url}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(By.CSS_SELECTOR, "#id_registration-email")
        password_input = self.browser.find_element(By.CSS_SELECTOR, "#id_registration-password1")
        confirm_password_input = self.browser.find_element(By.CSS_SELECTOR, "#id_registration-password2")
        register_button = self.browser.find_element(By.CSS_SELECTOR, "[name='registration_submit']")
        
        email_input.send_keys(email)
        password_input.send_keys(password)
        confirm_password_input.send_keys(password)
        register_button.click()