from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class GoogleSearch:
    def __init__(self, driver):
        self.name = "GoogleSearch"
        self.url = "https://google.com"
        self.driver = driver
        self.elements = dict(search_input="lst-ib",
                             apps_btn="gbwa",
                             gmail_btn="gb23")

    def google_search(self):
        self.driver.find_element_by_id(self.elements[
                                              "search_input"]).send_keys(
            "cats")
        self.driver.find_element_by_id(
            self.elements["search_input"]).send_keys(
            u'\ue007')

    def open_google_app(self, app):
        app_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.elements[
                "apps_btn"])))
        app_btn.click()
        if app == "gmail":
            self.driver.find_element_by_id(self.elements["gmail_btn"]).click()

