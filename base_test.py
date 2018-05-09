class BaseTest:
    def __init__(self):
        self.name = "BaseTest"

    def setup(self):
        print "setup"

    def teardown(self):
        print "teardown"
