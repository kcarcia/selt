import keyring
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class GoogleLogin:
    def __init__(self, driver):
        self.name = "GoogleLogin"
        self.url = "https://accounts.google.com/signin"
        self.driver = driver
        self.elements = dict(email_input="identifierId",
                             email_next_btn="identifierNext",
                             password_input="password",
                             password_next_btn="passwordNext")

    def google_login(self):
        self.driver.find_element_by_id(self.elements["email_input"]).send_keys(
            "test.dummy.1717@gmail.com")
        self.driver.find_element_by_id(self.elements["email_next_btn"]).click()
        password_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.NAME, self.elements[
                "password_input"])))
        password_input.send_keys(keyring.get_password("gmail", "testdummy"))
        self.driver.find_element_by_id(self.elements["password_next_btn"]).click()
