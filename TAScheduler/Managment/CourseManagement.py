# createCourse(courseName, courseTime, courseDays, courseHours, courseInstructor, courseTA)
# editCourse(courseName, courseTime, courseDays, courseHours, courseInstructor, courseTa)
# deleteCourse(courseName)
# populateSearchClass(searchPromp)  should change class to course
# displayAllCourse()
from types import coroutine
from django.db import models
from TAScheduler.models import Course
from TAScheduler.models import UserProfile
from django.shortcuts import render
class CourseManagement(object):

    # Preconditions: The user has to have been instantiated.
    # The user must be of type administrator
    # Postconditions:Creates a course
    # Side-effects: Course is created and added inside the database
    # Course Name(in) - Name of the course
    # Course Time(in) - Time of the course
    # Course Days(in) - Days of the course
    # Course Hoursin) - Hours of the course
    # Course Instructor(in) - Instructor of the course
    # Course TA(in) -TA of the course
    def createCourse(request, Id,courseName,courseLocation, courseDays, courseHours, courseInstructor, courseTAs, courseLabs):
        if(not(isinstance(Id, int))):
            raise TypeError("Id entered is not of type int")
        if(not(isinstance(courseName, str))):
            raise TypeError("Lab Name entered is not of type str")
        if(not(isinstance(courseLocation, str))):
            raise TypeError("Lab Location entered is not of type str")
        if(not(isinstance(courseDays, str))):
            raise TypeError("Lab Hours entered is not of type str")
        if(not(isinstance(courseHours, str))):
            raise TypeError("Lab Days entered is not of type str")
        if(not(isinstance(courseInstructor, UserProfile))):
            raise TypeError("Lab Instructor entered is not of type User")
        if(courseInstructor.userType != "INSTRUCTOR"):
            raise TypeError("Lab Instructor's type is not of type INSTRUCTOR")
        
        
        Course.objects.create(courseID=Id, name=courseName, location=courseLocation, 
        hours=courseHours, days=courseDays, instructor=courseInstructor, TAs=courseTAs, labs = courseLabs)

        return "Course was created"

    # Preconditions: The user has to have been instantiated.
    # The user must be of type administrator
    # Postconditions:Edits a course
    # Side-effects: Course is edited inside the database
    # Course Name(in) - Name of the course
    # Course Time(in) - Time of the course
    # Course Days(in) - Days of the course
    # Course Hoursin) - Hours of the course
    # Course Instructor(in) - Instructor of the course
    # Course TA(in) -TA of the course
    def editCourse(request, Id,courseName, courseLocation, courseDays, courseHours, courseInstructor, courseTAs, courseLabs):
        if(not(isinstance(Id, int))):
            raise TypeError("Id entered is not of type int")
        if(not(isinstance(courseName, str))):
            raise TypeError("Lab Name entered is not of type str")
        if(not(isinstance(courseLocation, str))):
            raise TypeError("Lab Location entered is not of type str")
        if(not(isinstance(courseDays, str))):
            raise TypeError("Lab Hours entered is not of type str")
        if(not(isinstance(courseHours, str))):
            raise TypeError("Lab Days entered is not of type str")
        if(not(isinstance(courseInstructor, UserProfile))):
            raise TypeError("Lab Instructor entered is not of type User")
        if(courseInstructor.userType != "INSTRUCTOR"):
            raise TypeError("Lab Instructor's type is not of type INSTRUCTOR")

        
        if(not(Course.objects.filter(courseId = Id).exists())):
            raise TypeError("This course does not exist")

        edittedCourse = Course.objects.get(courseId = Id)
        
        edittedCourse.name = courseName
        edittedCourse.location = courseLocation
        edittedCourse.hours = courseHours
        edittedCourse.days = courseDays
        edittedCourse.instructor = courseInstructor
        edittedCourse.TAs = courseTAs
        edittedCourse.labs = courseLabs

        return "The course was successfully editted"

    # Preconditions: The user has to have been instantiated.
    # The user must be of type administrator
    # Postconditions:Deletes a course
    # Side-effects: Course is deleted and removed from the database
    # Course Name(in) - Name of the course
    def deleteCourse(request, Id):
        if(not(isinstance(Id, int))):
            raise TypeError("Id entered is not of type int")

        retMsg = "Course has been successfully deleted"
        if(not(Course.objects.filter(courseId = Id).exists())):
            retMsg = "This Course being deleted does not exist"
        else:
            Course.objects.filter(courseId = Id).delete()

        return retMsg
    # Preconditions: The user has to have been instantiated
    # The searchPrompt is an existing course assignment name
    # Postconditions: Course assignments are populated
    # Side-effects: None
    # Search Prompt(in): Course Name you are searching for
    def populateSearchClass(request, Id):
        if(not(isinstance(Id, int))):
            raise TypeError("Id entered is not of type int")
        
        retMsg = ""
        if(not(Course.objects.filter(courseId = Id).exists())):
            retMsg = "This course being deleted does not exist"
        else:
            retMsg = {
                'Found Course': Course.objects.get(courseId = Id)
            }

        return retMsg

    # Preconditions: The user has to have been instantiated
    # There are courses to display
    # Postconditions: All courses are displayed
    # Side-effects: None
    def displayAllCourse(request):
        allCourses = Course.objects.all()

        data = {
            'All Courses': allCourses
        }
        
        return allCourses
