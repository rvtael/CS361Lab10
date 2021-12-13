class AssignmentManagement(object):

    def __init__(self, authID=""):
        pass

    # Preconditions: The user has to have been instantiated.
    # The user must be of type administrator or instructor
    # Postconditions:Creates a course assignment
    # Side-effects:Course assignment is created and added inside the database
    # Assignment Name(in) - Name of the course assignment
    # Assignment Due(in) - The due date of the assignment
    # Assignment Details(in) - Details of the assignment
    def createAssignmentCourse(self, assignmentName, assignmentDue, assignmentDetails):
        pass

    # Preconditions: The user has to have been instantiated.
    # The user must be of type administrator or instructor
    # Postconditions:Edits a course assignment
    # Side-effects:Course assignment is edited inside the database
    # Assignment Name(in) - Name of the course assignment
    # Assignment Due(in) - The due date of the assignment
    # Assignment Details(in) - Details of the assignment
    def editAssignmentCourse(self, assignmentName, assignmentDue, assignmentDetails):
        pass

    # Preconditions: The user has to have been instantiated.
    # The user must be of type administrator or instructor
    # The assignment being deleted must exist
    # Postconditions:Deletes a course assignment
    # Side-effects:Course assignment is deleted from the  database
    # Assignment Name(in) - Name of the course assignment
    def deleteAssignmentCourse(self, assignmentName):
        pass

    # Preconditions: The user has to have been instantiated.
    # The searchPrompt must be an existing course name
    # Postconditions:Populates course assignments with course name
    # Side-effects:None
    # Search Prompt(in) - Name of the course you are searching for
    def populateSearchCourse(self, searchPrompt):
        pass

    # Preconditions: The user has to have been instantiated.
    # The user must be of type administrator or instructor
    # Postconditions:Creates a TA assignment
    # Side-effects:TA assignment is created and added inside the database
    # Assignment Name(in) - Name of the TA assignment
    # Assignment Due(in) - The due date of the TA assignment
    # Assignment Details(in) - Details of the assignment
    def createAssignmentTA(self, assignmentName, assignmentDue, assignmentDetails):
        pass

    # Preconditions: The user has to have been instantiated.
    # The user must be of type administrator or instructor
    # Postconditions:Edits a TA assignment
    # Side-effects:TA assignment is edited inside the database
    # Assignment Name(in) - Name of the TA assignment
    # Assignment Due(in) - The due date of the assignment
    # Assignment Details(in) - Details of the assignment
    def editAssignmentTA(self, assignmentName, assignmentDue, assignmentDetails):
        pass

    # Preconditions: The user has to have been instantiated.
    # The user must be of type administrator or instructor
    # The assignment being deleted must exist
    # Postconditions:Deletes a TA assignment
    # Side-effects:TA assignment is deleted from the  database
    # Assignment Name(in) - Name of the TA assignment
    def deleteAssignmentTA(self, assignmentName):
        pass

    # Preconditions: The user has to have been instantiated.
    # The searchPrompt must be an existing course name
    # Postconditions:Populates TA assignments with course name
    # Side-effects:None
    # Search Prompt(in) - Name of the course you are searching for
    def populateSearchTA(self, searchPrompt):
        pass

    # Preconditions: The user has to have been instantiated.
    # Their are assignments to be displayed
    # Postconditions:Displays course assignments and TA assignments
    # Side-effects:None
    def populateSearchAll(self):
        pass
