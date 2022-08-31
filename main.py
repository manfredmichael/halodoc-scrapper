from selenium import webdriver
import time
import page
import tqdm
import json
from selenium.webdriver.chrome.options import Options

DRIVER_PATH = 'webdriver/chromedriver'

class HalodocMedicineScrapper():
    """A sample test class to show how page object works"""

    def setup(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(DRIVER_PATH, options=chrome_options)

    def collect_medicines(self):
        medicines = {
                "obat": []
            } 
        category_list_page = page.CategoryListPage(self.driver)
        category_urls = category_list_page.get_all_categories_url()
        for category_url in tqdm.tqdm(category_urls):
            medicine_list_page = page.MedicineListPage(self.driver, category_url)
            medicine_list_page.show_more_medicine()
            medicine_urls = medicine_list_page.get_all_medicine_url()
            for medicine_url in tqdm.tqdm(medicine_urls):
                medicine_page = page.MedicinePage(self.driver, medicine_url)
                info = medicine_page.get_info()
                medicines['obat'].append(info)
            with open('raw-result.json', 'w') as f:
                json.dump(medicines, f)




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


