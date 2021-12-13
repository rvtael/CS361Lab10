from django.db import models
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
    def createUser(self, Id, name, contact, address, password, email,usertype):
        if(not(isinstance(Id, int))):
            raise TypeError("Id entered is not of type int")
        if(not(isinstance(name, str))):
            raise TypeError("Name entered is not of type str")
        if(not(isinstance(contact, str))):
            raise TypeError("Contact entered is not of type str")
        if(not(isinstance(email, str))):
            raise TypeError("Email entered is not of type str")
        if(not(isinstance(address, str))):
            raise TypeError("Address entered is not of type str")
        if(not(isinstance(password, str))):
            raise TypeError("Password entered is not of type str")
        if(usertype != "TA" or usertype != "SUPERVISOR" or usertype != "INSTRUCTOR"):
            raise TypeError("Usertype entered is not proper type")

        if(self.findUser(Id) == "User not found"):
            UserProfile.objects.create(Id, name, contact, email, address, password, usertype)
            return("This user has been successfully added")
        else:
            return("This user already exists")
    # Preconditions: The user has to have been instantiated.
    # The user must be of type administrator
    # Postconditions: Edits a user
    # Side-effects: User is edited inside the database
    # UserId(in) - Id of the user
    # User Name(in) - Name of the user
    # User Contact(in) - Contact of the user

    # User Type(in) - Type of the user
    def editUser(self, Id, name, contact, email, address, password, usertype):
        if(not(isinstance(Id, int))):
            raise TypeError("Id entered is not of type int")
        if(not(isinstance(name, str))):
            raise TypeError("Name entered is not of type str")
        if(not(isinstance(contact, str))):
            raise TypeError("Contact entered is not of type str")
        if(not(isinstance(email, str))):
            raise TypeError("Email entered is not of type str")
        if(not(isinstance(address, str))):
            raise TypeError("Address entered is not of type str")
        if(not(isinstance(password, str))):
            raise TypeError("Address entered is not of type str")
        if(usertype != "TA" or usertype != "SUPERVISOR" or usertype != "INSTRUCTOR"):
            raise TypeError("Usertype entered is not proper type")

        if(not(UserProfile.objects.filter(userId = Id).exists())):
            return "This user already exists"

        edittedUser= UserProfile.objects.get(userId = Id)
        
        edittedUser.userType = usertype
        edittedUser.userName = name
        edittedUser.userPassword = password
        edittedUser.userAddress = address
        edittedUser.userContact = contact
        edittedUser.userEmail = email

        return "The user was successfully editted"
       

    # Preconditions: The user has to have been instantiated
    # There are accounts to display
    # Postconditions: Displays the user
    # Side-effects: None
    # UserId(in) - Id of the user
    def findUser(self, Id):
        if UserProfile.objects.filter(userID=Id).exists():
            data={
                'foundUser':UserProfile.objects.get(userID=Id)
            }
            return data
        else :

            data={
                "User not found"
            }

            return data
    # Preconditions: The user has to have been instantiated
    # The user must be of type administrator
    # Postconditions: User is deleted
    # Side-effects: User is deleted so it is removed from the database
    # UserId(in) - Id of the user
    def deleteUser(request, userID):

        if UserProfile.objects.filter(userID=userID).exists():
            UserProfile.objects.filter(userID=userID).delete()
            return "Succesfully deleted user"
        else:
            return "User doesn't exist"


    # Preconditions: The user has to have been instantiated
    # There are accounts to display
    # Postconditions: All accounts are displayed
    # Side-effects: None
    def populateList(self):
        allUsers = UserProfile.objects.all()

        data={
            'allUsers':allUsers
        }
        
        return allUsers

