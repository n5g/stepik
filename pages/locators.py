from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    #regisration
    EMAIL_REGISTRATION_FIELD =(By.NAME, "registration-email")
    PASSWORD_REGISTRATION_FIELD =(By.NAME, "registration-password1")
    PASSWORD_REPEAT_REGISTRATION_FIELD =(By.NAME, "registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")
    #enter
    ENTER_EMAIL_FIELD =(By.NAME, "login-username")
    ENTER_PASSWORD_FIELD =(By.NAME, "login-password")
    ENTER_BUTTON =(By.NAME, "login_submit")
