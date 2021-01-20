from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By


class MainPage(BasePage): 
	def go_to_login_page(self):
		login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK) #символ *, он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать.
		login_link.click()
		# Добавив обработку alert в метод go_to_login_page, мы восстановим работоспособность всех тестов, не меняя самих тестов:
		#alert = self.browser.switch_to.alert
		#Если вы попытаетесь перехватить диалоговое окно, которого нет, то получите исключение NoAlertPresentException.
		
	def should_be_login_link(self):
		assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"	#символ *, он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать.