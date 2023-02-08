from src.PageObject.Pages import GooglePage
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.GooglePage import GooglePage


class Test_scenario_1(WebDriverSetup):

    def test_add_text_to_scenario_1(self):
        driver = self.driver
        self.driver.get(GooglePage.get_base_url())
        home_page = GooglePage(driver)
        home_page.text_for_search("test automation")
        home_page.search()