import unittest
from entities.course import Course
from services.course_service import (
    CourseService
)
import db_helper


class TestCourseService(unittest.TestCase):
    def setUp(self):
        db_helper.drop_tables()
        db_helper.create_db()
        self.service = CourseService()

    def tearDown(self):
        self.service.conn.close()

    def test_course_creating_succeeds_and_returns_id(self):
        service = CourseService()
        course_id = service.create_course(user_id=1, name="testCourse", course_credits=5)
        self.assertEqual(1, course_id)

    def test_listing_current_courses_works(self):
        self.service.create_course(user_id=1, name="testCourse", course_credits=5)
        self.service.create_course(user_id=1, name="testCourse2", course_credits=5)
        courses = self.service.get_current_courses(user_id=1)
        self.assertEqual(list, type(courses))
        self.assertEqual(Course, type(courses[0]))
        self.assertEqual(2, len(courses))

    def test_course_deleting_succeeds(self):
        course_id = self.service.create_course(user_id=1, name="testCourse", course_credits=5)
        self.service.create_course(user_id=1, name="testCourse2", course_credits=5)
        self.service.delete_course(course_id=course_id)

        courses = self.service.get_current_courses(user_id=1)
        self.assertEqual(1, len(courses))
        self.assertEqual("testCourse2", courses[0].name)
