class GoogleSearch:
    def __init__(self):
        self.name = "GoogleSearch"
        self.elements = dict(search_box="//*[@id='lst-ib']")

    def google_search(self, driver):
        driver.get("https://google.com")
        driver.find_element_by_xpath(self.elements["search_box"]).send_keys(
            "cats")
        driver.find_element_by_xpath(self.elements["search_box"]).send_keys(
            u'\ue007')

