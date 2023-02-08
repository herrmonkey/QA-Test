import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

base_url = "https://google.com"


class GooglePage:
    def __init__(self, driver):
        self.driver = driver
        self.google_search = "/html/body/div[@class='L3eUgb']/div[@class='o3j99 ikrT4e om7nvf']/form/div[1]/div[@class='A8SBwf']/div[@class='RNNXgb']/div[@class='SDkEP']/div[@class='a4bIc']/input[@class='gLFyf']"
        self.search_button = "/html/body/div[@class='L3eUgb']/div[@class='o3j99 ikrT4e om7nvf']/form/div[1]/div[@class='A8SBwf']/div[@class='FPdoLc lJ9FBc']/center/input[@class='gNO89b']"
        self.find_results = "/html/body[@id='gsr']/div[@id='main']/div[@id='cnt']/div[@id='rcnt']/div[@id='center_col']/div[@id='res']/div[@id='search']/div/div[@id='rso']/div[@class='hlcw0c'][1]"

    def get_google_search(self):
        return self.driver.find_element(By.XPATH, self.google_search)

    def get_search_button(self):
        return self.driver.find_element(By.XPATH, self.search_button)

    def get_result_list(self):
        return self.driver.find_element(By.XPATH, self.find_results)

    def text_for_search(self, searched_text):
        self.get_google_search().send_keys(searched_text)
        self.get_google_search().send_keys(Keys.TAB)
        time.sleep(1)

    def search(self):
        self.get_search_button().click()

    def first_result(self):
        time.sleep(3)
        self.get_result_list().click()
    
    @staticmethod
    def get_base_url():
        return base_url