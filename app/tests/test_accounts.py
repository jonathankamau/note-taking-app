from app.tests.test_base import BaseTestClass

class TestSignUp(BaseTestClass):

    def test_user_is_registered(self):

        self.assertEqual(self.register.status_code, 200)

class TestLogin(BaseTestClass):

    def test_user_logged_in(self):

        self.assertEqual(self.user_login.status_code, 200)
