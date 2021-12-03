# createCourse(courseName, courseTime, courseDays, courseHours, courseInstructor, courseTA)
# editCourse(courseName, courseTime, courseDays, courseHours, courseInstructor, courseTa)
# deleteCourse(courseName)
# populateSearchClass(searchPromp)  should change class to course
# displayAllCourse()

class CourseManagement:

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
    @staticmethod
    def createCourse(courseName, courseTime, courseDays, courseHours, courseInstructor, courseTA):
        pass

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
    @staticmethod
    def editCourse(course, courseName, courseTime, courseDays, courseHours, courseInstructor, courseTA):
        pass

	# Preconditions: The user has to have been instantiated.
    # The user must be of type administrator
    # Postconditions:Deletes a course
	# Side-effects: Course is deleted and removed from the database
	# Course Name(in) - Name of the course
    @staticmethod
    def deleteCourse(course, courseName):
        pass

	# Preconditions: The user has to have been instantiated
	# The searchPrompt is an existing course assignment name
	# Postconditions: Course assignments are populated
	# Side-effects: None
	# Search Prompt(in): Course Name you are searching for
    @staticmethod
    def populateSearchClass(searchPromp):
        pass

	# Preconditions: The user has to have been instantiated
	# There are courses to display
	# Postconditions: All courses are displayed
	# Side-effects: None
    @staticmethod
    def displayAllCourse():
        pass
