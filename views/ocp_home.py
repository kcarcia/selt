class OcpHome:
    def __init__(self, driver):
        self.name = "OcpHome"
        self.driver = driver
        self.elements = dict(login_button="//*[@id='nav-main']/ul/li[6]/a")

    def test_go_to_ocp(self):
        """
        Polarion ID #: Verify the user can get to openshitft.com
        :return:
        """
        self.driver.get("https://www.openshift.com/")

    def test_login_to_ocp(self):
        """
        Polarion ID #: Verify the user is redirected the login screen.
        :return:
        """
        self.driver.find_element_by_xpath(self.elements["login_button"]).click()
