from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.options import DesiredCapabilities
import os
from configs.config import *


class BaseTest(object):
    def __init__(self, browser):
        self.name = "BaseTest"
        self.driver = ""
        self.browser = browser

    def setup(self):
        """
        Default setup method for tests. The browser is passed through the
        command line via the --browser flag OR the default browser specified
        in config.py is used.

        NOTE: Currently, init_browser supports only the latest version of
        Firefox and the latest version of Chrome. It  should be expanded to
        introduce more configurability and browser options. Additionally,
        parallelization is not yet supported.

        :param browser: (string) browser to run tests on
        :return:
        """
        if "firefox" in self.browser.lower():
            binary = FirefoxBinary(FIREFOX_PATH)
            firefox_capabilities = DesiredCapabilities.FIREFOX
            firefox_capabilities["marionette"] = True

            if "headless" in self.browser.lower():
                os.environ['MOZ_HEADLESS'] = '1'

            self.driver = webdriver.Firefox(firefox_binary=binary,
                                            executable_path=GECKODRIVER_PATH)
        elif "chrome" in self.browser.lower():
            chrome_options = Options()
            if "headless" in self.browser.lower():
                chrome_options.add_argument("--headless")

            self.driver = webdriver.Chrome(chrome_options=chrome_options,
                                           executable_path=CHROME_PATH)

    def teardown(self):
        """
        Default teardown method for tests. Close the browser.

        :return:
        """
        self.driver.quit()