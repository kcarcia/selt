from base_test import BaseTest
from views.google_search import GoogleSearch


class TestGoogleSearch(BaseTest):
    def __init__(self, browser):
        self.name = "TestGoogleSearch"
        super(TestGoogleSearch, self).__init__(browser)

    def setup(self):
        """
        Example of an overwritten setup method that leverages the default
        setup method.
        :return:
        """
        print "Example of an overwritten setup method that leverages the " \
              "default setup method"
        super(TestGoogleSearch, self).setup()

    def teardown(self):
        """
        Example of an overwritten teardown method.
        :return:
        """
        print "Example of an overwritten teardown method."

    def test_google_search(self, search_term="cats"):
        """
        Polarion ID #: Verify the user can search on google.
        :return:
        """
        google_search_view = GoogleSearch(self.driver)
        self.driver.get(google_search_view.url)
        google_search_view.google_search(search_term)

