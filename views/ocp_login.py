class OcpLogin:
    def __init__(self, driver):
        self.name = "OcpLogin"
        self.driver = driver
        self.elements = dict(login_with_rh="/html/body/div/div[2]/div[1]/a")

    def test_login_redirect(self):
        """
        Polarion ID #: Verify the user is redirected to the login page with
        the sign in form.
        :return:
        """
        self.driver.find_element_by_xpath(
            self.elements["login_with_rh"]).click()
