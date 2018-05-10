from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class GoogleDocsDashboard:
    def __init__(self, driver):
        self.name = "GoogleDocsDashboard"
        self.driver = driver
        self.elements = dict(new_btn="//*[@id='drive_main_page']/div["
                                         "2]/div/div[1]/div/div/div[3]/div["
                                         "1]/div/button[1]",
                             new_doc_btn="//*[contains(text(), 'Google "
                                         "Docs')]",
                             select_doc="//*[@id=':13']/div/div["
                                        "1]/div/div/div/div/div[2]/div/div",
                             copy_btn="//*[contains(text(), 'Make a copy')]")

    def create_document(self):
        self.driver.find_element_by_xpath(self.elements["new_btn"]).click()
        new_doc_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.elements[
                "new_doc_btn"])))
        new_doc_btn.click()
