class UserManagement(object):

    def __init__(self, authID=""):
        pass

    # Preconditions: The user has to have been instantiated.
    # The user must be of type administrator
    # Postconditions: Creates a user
    # Side-effects: User is created and added into the database
    # UserId(in) - Id of the user
    # User Name(in) - Name of the user
    # User Contact(in) - Contact of the user
    # User SSN(in) - SSN of the user
    # User Address(in) - Address of the user
    # User Password(in) - Password of the user
    # User Type(in) - Type of the user
    def createUser(self):
        pass

    # Preconditions: The user has to have been instantiated.
    # The user must be of type administrator
    # Postconditions: Edits a user
    # Side-effects: User is edited inside the database
    # UserId(in) - Id of the user
    # User Name(in) - Name of the user
    # User Contact(in) - Contact of the user
    # User SSN(in) - SSN of the user
    # User Address(in) - Address of the user
    # User Password(in) - Password of the user
    # User Type(in) - Type of the user
    def editUser(self):
        pass

    # Preconditions: The user has to have been instantiated
    # The user must be of type administrator
    # Postconditions: User is deleted
    # Side-effects: User is deleted so it is removed from the database
    # UserId(in) - Id of the user
    def deleteUser(self):
        pass

    # Preconditions: The user has to have been instantiated
    # There are accounts to display
    # Postconditions: Displays the user
    # Side-effects: None
    # UserId(in) - Id of the user
    def findUser(self):
        pass

    # Preconditions: The user has to have been instantiated
    # There are accounts to display
    # Postconditions: All accounts are displayed
    # Side-effects: None
    def populateList(self):
        pass
