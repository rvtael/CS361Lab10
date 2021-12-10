class LabManagement(object):

    def __init__(self, authID=""):
        pass

    # Preconditions: The user has to have been instantiated.
    # The user must be of type administrator
    # Postconditions:Creates a lab
    # Side-effects: Lab is created and added inside the database
    # Lab Name(in) - Name of the lab
    # Lab Hours(in) - Hours of the lab
    # Lab Location(in) - Location of the lab
    # Lab Days(in) - Days of the lab
    # Lab Instructor(in) - Instructor of the lab
    # Lab TA(in) -TA of the lab
    def createLab(self, labName, labHours, labLocation, labDays, labTA):
        pass

    # Preconditions: The user has to have been instantiated.
    # The user must be of type administrator
    # Postconditions:Edits a lab
    # Side-effects: Lab is edited inside the database
    # Lab Name(in) - Name of the lab
    # Lab Hours(in) - Hours of the lab
    # Lab Location(in) - Location of the lab
    # Lab Days(in) - Days of the lab
    # Lab Instructor(in) - Instructor of the lab
    # Lab TA(in) -TA of the lab
    def editLab(self, labName, labHours, labLocation, labDays, labTA):
        pass

    # Preconditions: The user has to have been instantiated.
    # The user must be of type administrator
    # Postconditions:Deletes a lab
    # Side-effects: Lab is deleted and removed from the database
    # Lab Name(in) - Name of the course
    def deleteLab(self, labName):
        pass

    # Preconditions: The user has to have been instantiated
    # The searchPrompt is an existing lab assignment name
    # Postconditions: Lab assignments are populated
    # Side-effects: None
    # Search Prompt(in): Lab Name you are searching for
    def populateSearchLab(self, searchPrompt):
        pass

    # Preconditions: The user has to have been instantiated
    # There are labs to display
    # Postconditions: All labs are displayed
    # Side-effects: None
    def displayAllLabs(self):
        pass
