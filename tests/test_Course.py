from unittest import TestCase
from course_lab_management.CourseManagement import CourseManagement
from course_lab_management.Course import Course
from user_and_login.User import User


# createCourse(courseName, courseTime, courseDays, courseHours, courseInstructor, courseTA)
# editCourse(courseName, courseTime, courseDays, courseHours, courseInstructor, courseTA)
# deleteCourse(courseName)
# populateSearchClass(searchPromp)  should change class to course
# displayAllCourse()

class TestCreateCourse(TestCase):

    def setUp(self):
        self.instructor = User
        self.TA = User
        self.testCourse = Course
        self.testCourse = CourseManagement.createCourse("Calculus", "12:00 PM", "M, W, F", "12:00 PM - 12:50 PM",
                                                        self.instructor, self.TA)

    def test_courseName(self):
        self.assertEqual("Calculus", self.testCourse.getCourseName(), "Course name was not set correctly when "
                                                                      "creating course.")

    def test_courseTime(self):
        self.assertEqual("12:00 PM", self.testCourse.getCourseTime(), "Course time was not set correctly when "
                                                                      "creating course.")

    def test_invalidTime(self):
        with self.assertRaises(ValueError,
                               msg="An exception was not raised when createCourse was passed an invalid time."):
            CourseManagement.createCourse("Course", "50:00", "M, W, F", "12:00 PM - 12:50 PM")

    def test_courseDays(self):
        self.assertEqual("M, W, F", self.testCourse.getCourseDays(), "Course days were not set correctly when "
                                                                     "creating course.")

    def test_invalidDays(self):
        with self.assertRaises(ValueError, msg="An exception was not raised when createCourse was passed invalid days."):
            CourseManagement.createCourse("Course", "12:00", "invalid input", "12:00 PM - 12:50 PM")

    def test_courseHours(self):
        self.assertEqual("12:00 PM - 12:50 PM", self.testCourse.getCourseHours(), "Course hours were not set "
                                                                                  "correctly when creating course.")

    def test_invalidHours(self):
        with self.assertRaises(ValueError, msg="An exception was not raised when createCourse was passed invalid hours."):
            CourseManagement.createCourse("Course", "12:00", "M, W, F", "invalid")

    def test_instructor(self):
        self.assertEqual(self.instructor, self.testCourse.getCourseInstructor(), "Course instructor was not set "
                                                                                 "correctly when creating course.")

    def test_invalidInstructor(self):
        with self.assertRaises(ValueError, msg="An exception was not raised when createCourse was passed an invalid "
                                               "instructor."):
            CourseManagement.createCourse("Course", "12:00", "M, W, F", "12:00 PM - 12:50 PM", "This shouldn't be this")

    def test_TA(self):
        self.assertEqual(self.TA, self.testCourse.getCourseTa(), "Course TA was not set correctly when creating course.")

    def test_invalidTA(self):
        with self.assertRaises(ValueError, msg="An exception was not raised when createCourse was passed an invalid TA."):
            CourseManagement.createCourse("Course", "12:00", "M, W, F", "12:00 PM - 12:50 PM", self.instructor, "String")
