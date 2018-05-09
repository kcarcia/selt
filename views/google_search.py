class GoogleSearch:
    def __init__(self):
        self.name = "GoogleSearch"
        self.elements = dict(search_box="//*[@id='lst-ib']")

    @staticmethod
    def google_search(driver):
        driver.get("https://google.com")
