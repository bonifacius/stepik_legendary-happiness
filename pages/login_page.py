from .base_page import BasePage
from .locators import LoginPageLocators



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        ls_link = self.browser.current_url 
        assert "login" in ls_link, "word 'login' is not in url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.ADDRESS_EMAIL), "ADDRESS_EMAIL form is not presented"
        assert self.is_element_present(*LoginPageLocators.USER_PASSWORD), "USER_PASSWORD form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_ADDRESS_EMAIL), "REGISTRATION_ADDRESS_EMAIL is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_USER), "REGISTRATION_PASSWORD_USER is not presented"
        assert self.is_element_present(*LoginPageLocators.REPEAT_PASSWORD_ADDRESS_EMAIL), "REPEAT_PASSWORD_ADDRESS_EMAIL is not presented"