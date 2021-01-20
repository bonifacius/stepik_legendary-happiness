from selenium.webdriver.common.by import By

# #Выносим селектор во внешний класс, для удобства редактирования. 
# Далее в метод будет передаваться кортеж *MainPageLocators.LOGIN_LINK из двух строк(вид и название селектора)
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	# селексторы для поля "Войти"
	ADDRESS_EMAIL = (By.CSS_SELECTOR, "id_login_username")  
	USER_PASSWORD = (By.CSS_SELECTOR, "id_login_password")
	
	# селексторы для поля "Зарегистрироваться"
	REGISTRATION_ADDRESS_EMAIL = (By.CSS_SELECTOR, "id_registration_email")
	REGISTRATION_PASSWORD_USER = (By.CSS_SELECTOR, "id_registration_password")
	REPEAT_PASSWORD_ADDRESS_EMAIL = (By.CSS_SELECTOR, "id_registration_password2")

