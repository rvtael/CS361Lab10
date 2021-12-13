from TAScheduler.models import UserProfile


class UserManagement(object):

    # Preconditions: The user has to have been instantiated.
    # The user must be of type administrator
    # Postconditions: Creates a user
    # Side-effects: User is created and added into the database
    # UserId(in) - Id of the user
    # User Name(in) - Name of the user
    # User Contact(in) - Contact of the user
    # User Type(in) - Type of the user
    @staticmethod
    def createUser(Id, name, contact, address, password, email, usertype):
        UserManagement.__inputErrorCheck(Id, name, contact, address, password, email, usertype)

        try:
            UserManagement.findUser(Id)
        except TypeError:
            UserProfile.objects.create(
                userID=Id,
                userType=usertype,
                userPassword=password,
                userName=name,
                userAddress=address,
                userContact=contact,
                userEmail=email
            )
            return

        raise TypeError("This user already exists: ")

    # Preconditions: The user has to have been instantiated.
    # The user must be of type administrator
    # Postconditions: Edits a user
    # Side-effects: User is edited inside the database
    # UserId(in) - Id of the user
    # User Name(in) - Name of the user
    # User Contact(in) - Contact of the user

    # User Type(in) - Type of the user
    @staticmethod
    def editUser(Id, name, contact, email, address, password, usertype):
        UserManagement.__inputErrorCheck(Id, name, contact, email, address, password, usertype)

        try:
            UserManagement.findUser(Id)
        except TypeError:
            raise TypeError("This user already exists(editUser): ")

    # Preconditions: The user has to have been instantiated
    # There are accounts to display
    # Postconditions: Displays the user
    # Side-effects: None
    # UserId(in) - Id of the user
    @staticmethod
    def findUser(Id):
        if not (isinstance(Id, int)):
            raise TypeError("Id entered is not of type int")
        try:
            profile = UserProfile.objects.get(userID=Id)
        except UserProfile.DoesNotExist:
            profile = None

        if profile is None:
            raise TypeError("This ID does not exist")

        return profile

    # Preconditions: The user has to have been instantiated
    # The user must be of type administrator
    # Postconditions: User is deleted
    # Side-effects: User is deleted so it is removed from the database
    # UserId(in) - Id of the user
    @staticmethod
    def deleteUser(Id):
        UserManagement.findUser(Id).delete()

    # Preconditions: The user has to have been instantiated
    # There are accounts to display
    # Postconditions: All accounts are displayed
    # Side-effects: None
    @staticmethod
    def populateList():
        pass

    @staticmethod
    def __inputErrorCheck(Id, name, contact, email, address, password, usertype):
        if not (isinstance(Id, int)):
            raise TypeError("Id entered is not of type int")
        if not (isinstance(name, str)):
            raise TypeError("Name entered is not of type str")
        if not (isinstance(contact, str)):
            raise TypeError("Contact entered is not of type str")
        if not (isinstance(email, str)):
            raise TypeError("Email entered is not of type str")
        if not (isinstance(address, str)):
            raise TypeError("Address entered is not of type str")
        if not (isinstance(password, str)):
            raise TypeError("Password entered is not of type str")
        if not (isinstance(usertype, str)):
            raise TypeError("userType entered is not of type str")
        if not(usertype in ["SUPERVISOR", "INSTRUCTOR", "TA"]):
            raise ValueError("userType entered is not a valid userType")
