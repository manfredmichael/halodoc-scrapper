from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    USERNAME_TEXT_INPUT = (By.ID, 'username')
    PASSWORD_TEXT_INPUT = (By.ID, 'password')

class CategoryListPageLocators(object):
    CATEGORY_BUTTON = (By.CSS_SELECTOR, "a[class='d-flex flex-fill flex-row align-items-center ng-star-inserted']")
