from typing import Type
from TAScheduler.User.UserType import UserType
# setId()
# setName()
# setContact()
# setSSN()
# setAddress()
# setPassword()
# setType()
#
# getType()
# getId()
# getName()
# getContact()
# getSSN()
# getAddress()
# getPassword()



class User(UserType):

    def __init__(self, Id, name, contact, SSN, address, password, type):
        if(not(isinstance(Id, int))):
            raise TypeError("Id entered is not of type int")
        if(not(isinstance(name, str))):
            raise TypeError("Name entered is not of type str")
        if(not(isinstance(contact, str))):
            raise TypeError("Contact entered is not of type str")
        if(not(isinstance(SSN, int))):
            raise TypeError("SSN entered is not of type int")
        if(not(isinstance(address, str))):
            raise TypeError("Address entered is not of type str")
        if(not(isinstance(type, int))):
            raise TypeError("SSN entered is not of type int")
        if(type <= 0 or type > 3):
            raise ValueError("Type is out of range - 1: TA 2: Instructor 3: Administrator")
        self.Id = Id
        self.name = name
        self.contact = contact
        self.SSN = SSN
        self.address = address 
        self.password = password
        self.type = type

    # Preconditions: The user has to have been instantiated
    # Postconditions: Sets the id of the user
    # Side-effects: None
    # User ID(in) - Id of the user
    def setId(self, Id):
        if(not(isinstance(Id, int))):
            raise TypeError("Id entered is not of type int")
        self.Id = Id

    # Preconditions: The user has to have been instantiated
    # Postconditions: Sets the name of the user
    # Side-effects: None
    # User Name(in) - Name of the user
    def setName(self, name):
        if(not(isinstance(name, str))):
            raise TypeError("Name entered is not of type str")
        self.name = name

	# Preconditions: The user has to have been instantiated
	# Postconditions: Sets the contact of the user
	# Side-effects: None
	# User Contact(in) - Contact of the user
    def setContact(self, contact):
        if(not(isinstance(contact, str))):
            raise TypeError("Contact entered is not of type str")
        self.contact = contact

    # Preconditions: The user has to have been instantiated
    # Postconditions: Sets the SSN of the user
    # Side-effects: None
    # User SSN(in) - SSN of the user
    def setSSN(self, SSN):
        if(not(isinstance(SSN, int))):
            raise TypeError("SSN entered is not of type int")
        self.SSN = SSN

	# Preconditions: The user has to have been instantiated
	# Postconditions: Sets the address of the user
	# Side-effects: None
	# User Address(in) - Address of the user
    def setAddress(self, address):
        if(not(isinstance(address, str))):
            raise TypeError("Address entered is not of type str")
        self.address = address

	# Preconditions: The user has to have been instantiated
	# Postconditions: Sets the password of the user
	# Side-effects: None
	# User Password(in) - Password of the user
    def setPassword(self, password):
        if(not(isinstance(password, str))):
            raise TypeError("Password entered is not of type str")
        self.password = password

    # Preconditions: The user has to have been instantiated
	# Postconditions: Sets the Type of the user
	# Side-effects: None
	# User Type(in) - Type of the use
    def setType(self, type):
        if(not(isinstance(type, int))):
            raise TypeError("SSN entered is not of type int")
        if(type <= 0 or type > 3):
            raise ValueError("Type is out of range - 1: TA 2: Instructor 3: Administrator")
        self.type = type

	# Preconditions: The user has to have been instantiated
	# Postconditions: Gets the id of the user
	# Side-effects: None
	# User ID(in) - Id of the user
    def getId(self):
        return self.Id

	# Preconditions: The user has to have been instantiated
	# Postconditions: Gets the name of the user
	# Side-effects: None
	# User Name(out) - Name of the user
    def getName(self):
        return self.name

	# Preconditions: The user has to have been instantiated
	# Postconditions: Gets the contact of the user
	# Side-effects: None
	# User Contact(out) - Contact of the user
    def getContact(self):
        return self.contact

	# Preconditions: The user has to have been instantiated
	# Postconditions: Gets the SSN of the user
	# Side-effects: None
	# User SSN(out) - SSN of the user
    def getSSN(self):
        return self.SSN

	# Preconditions: The user has to have been instantiated
	# Postconditions: Gets the address of the user
	# Side-effects: None
	# User Address(out) - Address of the user
    def getAddress(self):
        return self.address

    # Preconditions: The user has to have been instantiated
    # Postconditions: Gets the password of the user
    # Side-effects: None
    # User Password(out) - Password of the user
    def getPassword(self):
        return self.password

    # Preconditions: The user has to have been instantiated
    # Postconditions: Gets the Type of the user
    # Side-effects: None
    # User Type(out) - Type of the user
    def getType(self):
        return self.type
