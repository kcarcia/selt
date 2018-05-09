from views.google_login import GoogleLogin
from views.google_docs_dashboard import GoogleDocsDashboard


class TestDeleteDoc:
    def __init__(self, driver):
        self.name = "TestDeleteDoc"
        self.driver = driver

    def test_delete_doc(self):
        """
        Polarion ID #: Verify the user can login their account and
        create a google document.
        :return:
        """
        login_view = GoogleLogin("")
        dashboard_view = GoogleDocsDashboard("")
        login_view.google_login()
        dashboard_view.delete_document()

