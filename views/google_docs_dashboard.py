class GoogleDocsDashboard:
    def __init__(self, driver):
        self.name = "GoogleDocsDashboard"
        self.driver = driver
        self.elements = dict(login_with_rh="/html/body/div/div[2]/div[1]/a")

    def create_document(self):
        # self.driver.find_element_by_xpath(
        #     self.elements["login_with_rh"]).click()
        print "User can create a google document."

    def delete_document(self):
        # self.driver.find_element_by_xpath(
        #     self.elements["login_with_rh"]).click()
        print "User can delete a google document."