from views.google_login import GoogleLogin
from views.google_search import GoogleSearch
from views.google_docs_dashboard import GoogleDocsDashboard
from base_test import BaseTest


class TestCreateDoc(BaseTest):
    def __init__(self, browser):
        self.name = "TestCreateDoc"
        super(TestCreateDoc, self).__init__(browser)

    def teardown(self):
        print "not tearing down"

    def test_create_doc(self):
        """
        Polarion ID #: Verify the user can login their account and
        create a google document.
        :return:
        """
        login_view = GoogleLogin(self.driver)
        docs_dashboard_view = GoogleDocsDashboard(self.driver)
        google_search_view = GoogleSearch(self.driver)

        self.driver.get(login_view.url)
        login_view.google_login()
        google_search_view.open_google_app("drive")
        docs_dashboard_view.create_document()
