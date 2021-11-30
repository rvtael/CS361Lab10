class LabManagement(object):
    """Reduced fraction class with integer numerator and denominator."""

    def __init__(self, authID=""):
      pass

    # Precondition:Lab does not already exist, all parameters are entered (save for instructor or courseTA). All parameters are valid
    # Postcondition:Lab is created
    def createLab(self, labName, labHours, labLocation, labDays, labTA):
        pass

    # Precondition: Lab exists, all parameters are valid
    # Postcondition: Lab is edited given parameters.
    def editLab(self, labName, labHours, labLocation, labDays, labTA):
        pass

    # Precondition:The Lab exists
    # Postcondition:The Lab is deleted
    def deleteLab(self, labName):
        pass

    # Precondition: Search prompt is not null
    # Postcondition: Lab with similar names will populate
    def populateSearchLab(self, searchPrompt):
        pass

    # Precondition: There are courses to display
    # Postcondition: All courses are populated
    def displayAllLabs(self):
        pass
