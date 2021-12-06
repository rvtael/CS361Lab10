from django.test import TestCase
from django.test import Client
from TAScheduler.NonDjangoClasses.course_lab_management.CourseManagement import CourseManagement
from TAScheduler.models import Course
from TAScheduler.models import UserProfile


# createCourse(courseName, courseTime, courseDays, courseHours, courseInstructor, courseTA)
# editCourse(courseName, courseTime, courseDays, courseHours, courseInstructor, courseTA)
# deleteCourse(courseName)
# populateSearchClass(searchPromp)  should change class to course
# displayAllCourse()

class TestCreateCourse(TestCase):

    def setUp(self):
        self.instructor = UserProfile
        self.TA = UserProfile
        CourseManagement.createCourse("Calculus", "12:00 PM", "M, W, F", "12:00 PM - 12:50 PM", self.instructor, self.TA)
        self.testCourse = Course.objects.get(courseName="Calculus")

    def test_courseName(self):
        self.assertEqual("Calculus", self.testCourse.getCourseName(), "Course name was not set correctly when "
                                                                      "creating course.")

    def test_courseTime(self):
        self.assertEqual("12:00 PM", self.testCourse.getCourseTime(), "Course time was not set correctly when "
                                                                      "creating course.")

    def test_invalidTime(self):
        with self.assertRaises(ValueError, msg="An exception was not raised when createCourse was passed an invalid "
                                               "time."):
            CourseManagement.createCourse("Course", "50:00", "M, W, F", "12:00 PM - 12:50 PM")

    def test_courseDays(self):
        self.assertEqual("M, W, F", self.testCourse.getCourseDays(), "Course days were not set correctly when "
                                                                     "creating course.")

    def test_invalidDays(self):
        with self.assertRaises(ValueError,
                               msg="An exception was not raised when createCourse was passed invalid days."):
            CourseManagement.createCourse("Course", "12:00", "invalid input", "12:00 PM - 12:50 PM")

    def test_courseHours(self):
        self.assertEqual("12:00 PM - 12:50 PM", self.testCourse.getCourseHours(), "Course hours were not set "
                                                                                  "correctly when creating course.")

    def test_invalidHours(self):
        with self.assertRaises(ValueError,
                               msg="An exception was not raised when createCourse was passed invalid hours."):
            CourseManagement.createCourse("Course", "12:00", "M, W, F", "invalid")

    def test_instructor(self):
        self.assertEqual(self.instructor, self.testCourse.getCourseInstructor(), "Course instructor was not set "
                                                                                 "correctly when creating course.")

    def test_invalidInstructor(self):
        with self.assertRaises(TypeError, msg="An exception was not raised when createCourse was passed an invalid "
                                              "instructor."):
            CourseManagement.createCourse("Course", "12:00", "M, W, F", "12:00 PM - 12:50 PM", "This shouldn't be this")

    def test_TA(self):
        self.assertEqual(self.TA, self.testCourse.getCourseTa(),
                         "Course TA was not set correctly when creating course.")

    def test_invalidTA(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when createCourse was passed an invalid TA."):
            CourseManagement.createCourse("Course", "12:00", "M, W, F", "12:00 PM - 12:50 PM", self.instructor,
                                          "String")


class TestEditCourse(TestCase):

    def setUp(self):
        self.instructor = UserProfile
        self.instructor2 = UserProfile
        self.TA = UserProfile
        self.TA2 = UserProfile
        # Course for invalid inputs
        Course(courseName="Calculus", courseTime="12:00 PM", courseDays="M, W, F", courseInstructor=self.instructor,
               courseTA=self.TA).save()
        # Course for editName
        Course(courseName="Computer Programming", courseTime="1:00 PM", courseDays="T, Th",
               courseInstructor=self.instructor2, courseTA=self.TA2).save()
        # Course for everything else
        Course(courseName="History", courseTime="5:00 PM", courseDays="M, T, W", courseInstructor=self.instructor,
               courseTA=self.TA)

    def test_editName(self):
        mathCourse = Course.objects.get(courseName="Computer Programming")
        CourseManagement.editCourse(mathCourse, courseName="Trigonometry")
        self.assertEqual("Trigonometry", mathCourse.courseName, "Name was not edited correctly.")

    def test_editTime(self):
        historyCourse = Course.objects.get(courseName="History")
        CourseManagement.editCourse(historyCourse, courseTime="2:00 PM")
        self.assertEqual("2:00 PM", historyCourse.courseTime, "Time was not edited correctly.")

    def test_invalidTime(self):
        mathCourse = Course.objects.get(courseName="Calculus")
        with self.assertRaises(ValueError,
                               msg="An exception was not raises when editCourse was passed an invalid time."):
            CourseManagement.editCourse(mathCourse, courseTime="25:00 PM")
        self.assertEqual("12:00 PM", mathCourse.courseTime, "editCourse changed courseTime when it shouldn't have.")

    def test_editDays(self):
        historyCourse = Course.objects.get(courseName="History")
        CourseManagement.editCourse(historyCourse, courseDays="S, Su")
        self.assertEqual("S, Su", historyCourse.courseDays, "Days were not edited correctly.")

    def test_invalidDays(self):
        mathCourse = Course.objects.get(courseName="Calculus")
        with self.assertRaises(ValueError, msg="An exception was not raised when editCourse was passed bad days."):
            CourseManagement.editCourse(mathCourse, courseDays="Invalid")
        self.assertEqual("M, W, F", mathCourse.courseDays, "editCourse changed courseDays when they shouldn't have.")

    def test_editInstructor(self):
        historyCourse = Course.objects.get(courseName="History")
        CourseManagement.editCourse(historyCourse, courseInstructor=self.instructor2)
        self.assertEqual(self.instructor2, historyCourse.courseInstructor, "Instructor was not edited correctly.")

    def test_invalidInstructor(self):
        mathCourse = Course.objects.get(courseName="Calculus")
        with self.assertRaises(TypeError, msg="A TypeError was not raised when editCourse was passed an invalid type "
                                              "for courseInstructor."):
            CourseManagement.editCourse(mathCourse, courseInstructor="TotallyAnInstructorIPromise")
        self.assertEqual(self.instructor, mathCourse.courseInstructor, "editCourse changed instructor when it "
                                                                       "shouldn't have.")

    def test_editTA(self):
        historyCourse = Course.objects.get(courseName="History")
        CourseManagement.editCourse(historyCourse, courseTA=self.TA2)
        self.assertEqual(self.TA2, historyCourse.courseTA, "TA was not edited correctly.")

    def test_invalidTA(self):
        mathCourse = Course.objects.get(courseName="Calculus")
        with self.assertRaises(TypeError,
                               msg="A TypeError was not raised when editCourse was passed an invalid type for courseTA."):
            CourseManagement.editCourse(mathCourse, courseTA="TotallyATAIPromise")
        self.assertEqual(self.TA, mathCourse.TA,
                         "editCourse changed TA when it shouldn't have.")


class TestDeleteCourse(TestCase):
    def setUp(self):
        self.instructor = UserProfile
        self.TA = UserProfile
        Course(courseName="Art", courseTime="12:00 PM", courseDays="M, W, F", courseHours="12:00 PM - 12:50 PM", courseInstructor=self.instructor, courseTA=self.TA).save()

    def test_delete(self):
        oldCourse = Course.objects.get(courseName="Art")
        CourseManagement.deleteCourse(oldCourse)
        self.assertEqual(None, oldCourse, "Course was not deleted successfully.")
