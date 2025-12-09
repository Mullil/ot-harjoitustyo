import unittest
from services.user_service import (
    UserService, UsernameExistsError, InvalidPasswordError, InvalidCredentialsError
)
import db_helper


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.username = "username"
        self.password = "password"
        db_helper.drop_tables()
        db_helper.create_db()
        self.service = UserService()

    def tearDown(self):
        self.service.conn.close()

    def test_registration_succeeds(self):
        self.assertTrue(self.service.register(
            self.username, self.password, "password"))

    def test_registration_fails_with_short_password(self):
        self.assertRaises(InvalidPasswordError,
                          lambda: self.service.register("username", "p", "p"))

    def test_registration_fails_if_username_exists(self):
        self.service.register(self.username, self.password, self.password)
        self.assertRaises(UsernameExistsError, lambda: self.service.register(
            self.username, "anotherpassword", "anotherpassword"))

    def test_registration_fails_if_passwords_dont_match(self):
        self.assertRaises(InvalidPasswordError, lambda: self.service.register(
            self.username, "password", "anotherpassword"))

    def test_login_succeeds(self):
        self.service.register(self.username, self.password, "password")
        self.assertTrue(self.service.login(self.username, self.password))
        self.assertEqual(self.service.current_user.username, "username")

    def test_login_fails_with_invalid_credentials(self):
        self.service.register(self.username, self.password, "password")
        self.assertRaises(InvalidCredentialsError,
                          lambda: self.service.login(self.username, "wrong"))
