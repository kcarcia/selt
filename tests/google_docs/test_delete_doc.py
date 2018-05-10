from views.google_login import GoogleLogin
from views.google_search import GoogleSearch
from views.google_docs_dashboard import GoogleDocsDashboard
from base_test import BaseTest


class TestDeleteDoc(BaseTest):
    def __init__(self, browser):
        self.name = "TestDeleteDoc"
        super(TestDeleteDoc, self).__init__(browser)

    def test_delete_doc(self):
        """
        Polarion ID #: Verify the user can login their account and
        create a google document.
        :return:
        """
        print "Delete document."
