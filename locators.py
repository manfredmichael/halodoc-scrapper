from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    USERNAME_TEXT_INPUT = (By.ID, 'username')
    PASSWORD_TEXT_INPUT = (By.ID, 'password')

class CategoryListPageLocators(object):
    CATEGORY_BUTTON = (By.CSS_SELECTOR, "a[class='d-flex flex-fill flex-row align-items-center ng-star-inserted']")
    
class MedicineListPageLocators(object):
    MEDICINE_BUTTON = (By.CSS_SELECTOR, "a[class='custom-container__list__container__item--link ng-star-inserted']")
    SHOW_MORE_BUTTON = (By.CSS_SELECTOR, "button[class='custom-container__pagination--btn']")
