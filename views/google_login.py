class GoogleLogin:
    def __init__(self, driver):
        self.name = "OcpHome"
        self.driver = driver
        self.elements = dict(login_button="//*[@id='nav-main']/ul/li[6]/a")

    def google_login(self):
        print "Google user can login into their account."
