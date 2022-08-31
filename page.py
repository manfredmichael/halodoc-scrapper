import time
import utils
import element

from selenium.common.exceptions import NoSuchElementException

class BasePage(object):
    """ Base class to initialize the base page that will be called from all pages """

    def __init__(self, driver):
        self.driver = driver
        self.open()

    def open(self):
        self.driver.get(self.URL)


class CategoryListPage(BasePage):
    """ A page object to browse all medicine categories """

    URL = 'https://www.halodoc.com/obat-dan-vitamin'
    categories = element.CategoryButtonMultiElement()

    def get_all_categories_url(self):
        """ Return all medicine category urls """
        
        urls = []
        for category in self.categories:
            urls.append(category.get_attribute("href"))
        return urls


class MedicineListPage(BasePage):
    """ A page object to browse all medicine in a category """
    medicines = element.MedicineButtonMultiElement()

    def __init__(self, drive, url):
        self.URL = url
        super().__init__(drive)

    def get_all_medicine_url(self):
        urls = []
        for medicine in self.medicines:
            urls.append(medicine.get_attribute("href"))
            # urls.append()
        print(urls)
        return urls

    def show_more_medicine(self):
        while self.can_scroll():
            time.sleep(3)
            self.scroll()

    def scroll(self):
        element.ShowMoreButtonElement()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def can_scroll(self):
        try:
            element.ShowMoreButtonElement()
            return True
        except NoSuchElementException:
            return False

    def get_height(self):
        return self.driver.execute_script("return document.body.scrollHeight")


class SearchPage(BasePage):
    URL = 'https://www.linkedin.com/search/results/content/?keywords=achievement&sid=w9B'
    height = None 

    def collect_all_post(self):
        self.show_more_post()

    def show_more_post(self):
        while self.can_scroll():
            time.sleep(3)
            self.scroll()

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def can_scroll(self):
        if self.height is None:
            self.height = self.get_height() 
            return True

        height_current = self.height
        height_new = self.get_height() 
        self.height = height_new
        return height_current != height_new 

    def get_height(self):
        return self.driver.execute_script("return document.body.scrollHeight")
