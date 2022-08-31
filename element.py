from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators

class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""

        driver = obj.driver
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located(self.locator))
        element.clear()
        element.send_keys(value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""

        driver = obj.driver
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located(self.locator))
        return element

    def __str__(self, obj, owner):
        """Gets the text of the specified object"""

        driver = obj.driver
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located(self.locator))
        return element.text

class BasePageMultiElement(BasePageElement):
    """Base page class that is initialized on every page object class."""

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""

        driver = obj.driver
        element = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located(self.locator))
        return element

    def __str__(self, obj, owner):
        """Gets the text of the specified object"""

        driver = obj.driver
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located(self.locator))
        return element.text



class UsernameInputElement(BasePageElement):
    locator = locators.LoginPageLocators.USERNAME_TEXT_INPUT

class PasswordInputElement(BasePageElement):
    locator = locators.LoginPageLocators.PASSWORD_TEXT_INPUT

class CategoryButtonMultiElement(BasePageMultiElement):
    locator = locators.CategoryListPageLocators.CATEGORY_BUTTON
