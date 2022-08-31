import time
import utils
import element

from selenium.common.exceptions import NoSuchElementException, TimeoutException



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
    show_more_button = element.ShowMoreButtonElement()

    def __init__(self, drive, url):
        self.URL = url
        super().__init__(drive)

    def get_all_medicine_url(self):
        """ Return all medicine urls """

        urls = []
        for medicine in self.medicines:
            urls.append(medicine.get_attribute("href"))

        return urls

    def show_more_medicine(self):
        while True:
            time.sleep(3)
            try:
                self.scroll()
            except TimeoutException:
                break

    def scroll(self):
        self.show_more_button.click()


    def get_height(self):
        return self.driver.execute_script("return document.body.scrollHeight")


class MedicinePage(BasePage):
    """ A page object fetch medicine information """
    
    title = element.MedicineTitleElement()
    descriptions = element.MedicineDescriptionMultiElement()

    def __init__(self, drive, url):
        self.URL = url
        super().__init__(drive)

    def get_info(self):
        """ Return scrapped information texts in dict """
        obat = {}
        obat['title'] = self.title.text
        obat['description'] = {}
        for description in self.descriptions:
            key = description.text.split('\n')[0]
            value = '\n'.join(description.text.split('\n')[1:])
            obat['description'][key] = value

        return obat

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
