from base_test import BaseTest


class TestGoogleSearch(BaseTest):
    def __init__(self, driver):
        self.name = "TestGoogleSearch"
        self.driver = driver

    def setup(self):
        print "overriden setup"

    def test_google_search(self):
        """
        Polarion ID #: Verify the user can search on google.
        :return:
        """
        print "User can search."

