from selenium import webdriver
import time
import page

DRIVER_PATH = 'webdriver/chromedriver'

class HalodocMedicineScrapper():
    """A sample test class to show how page object works"""

    def setup(self):
        self.driver = webdriver.Chrome(DRIVER_PATH)

    def collect_medicines(self):
        category_list_page = page.CategoryListPage(self.driver)
        category_list_page.get_all_categories_url()

        # search_page.show_more_post()

    def run(self):
        self.setup()
        # self.login()
        self.collect_medicines()

    def tear_down(self):
        self.driver.close()

if __name__ == '__main__':
    scrapper = HalodocMedicineScrapper()
    try:
        scrapper.run()
    finally:
        time.sleep(5)
        scrapper.tear_down()


