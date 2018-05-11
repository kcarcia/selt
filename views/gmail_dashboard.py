from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class GmailDashboard:
    def __init__(self, driver):
        self.name = "GmailDashboard"
        self.driver = driver
        self.elements = dict(compose_btn="//*[@id=':3w']/div/div",
                             email_recipient="//textarea[@aria-label='To']",
                             close_btn=":5m",
                             draft_link="//*[@id=':49']/div/div[2]/span/a",
                             select_all_checkbox="//*[@id=':60']",
                             discard_draft_btn="//div["
                                               "@aria-label='Discard draft']")

    def compose_email(self):
        self.driver.find_element_by_xpath(self.elements["compose_btn"]).click()
        email_recipient = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.elements[
                "email_recipient"])))
        email_recipient.send_keys(
            "test")
        self.driver.find_element_by_id(self.elements["close_btn"]).click()

    def delete_email_draft(self):
        actions = ActionChains(self.driver)
        self.driver.find_element_by_xpath(self.elements["draft_link"]).click()
        select_all_checkbox = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.elements[
                "select_all_checkbox"])))
        actions.move_to_element(select_all_checkbox).click().perform()
        discard_draft_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.elements[
                "discard_draft_btn"])))
        discard_draft_btn.click()
        time.sleep(1)
        self.driver.refresh()
