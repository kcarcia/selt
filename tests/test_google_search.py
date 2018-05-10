from base_test import BaseTest
from views.google_search import GoogleSearch


class TestGoogleSearch(BaseTest):
    def __init__(self, browser):
        self.name = "TestGoogleSearch"
        super(TestGoogleSearch, self).__init__(browser)

    def test_google_search(self):
        """
        Polarion ID #: Verify the user can search on google.
        :return:
        """
        google_search_view = GoogleSearch()
        google_search_view.google_search(self.driver)

