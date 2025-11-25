import unittest
from services.course_service import (
    CourseService
)
import db_helper

"""
class TestCourseService(unittest.TestCase):
    def setUp(self):
        db_helper.drop_tables()
        db_helper.create_db()

    def test_course_creating_succeeds(self):
        service = CourseService()
        self.assertTrue(service.register(
            self.username, self.password, "password"))

    def test_course_creating_fails_with_missing_values(self):
        service = CourseService()
        self.assertRaises(InvalidPasswordError,
                          lambda: service.register("username", "p", "p"))

    def test_course_deleting_succeeds(self):
        service = CourseService()
        service.register(self.username, self.password, self.password)
        self.assertRaises(CoursenameExistsError, lambda: service.register(
            self.username, "anotherpassword", "anotherpassword"))

    def test_course_completing_succeeds(self):
        service = CourseService()
        self.assertRaises(InvalidPasswordError, lambda: service.register(
            self.username, "password", "anotherpassword"))

    def test_listing_current_courses_works(self):
        service = CourseService()
        service.register(self.username, self.password, "password")
        self.assertTrue(service.login(self.username, self.password))
        self.assertEqual(service.current_user.username, "username")

    def test_listing_completed_courses_words(self):
        service = CourseService()
        service.register(self.username, self.password, "password")
        self.assertRaises(InvalidCredentialsError,
                          lambda: service.login(self.username, "wrong"))

    def test_correct_amount_of_credits_are_returned(self):
        service = CourseService()
        self.assertTrue(service.register(
            self.username, self.password, "password"))

"""
