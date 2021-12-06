from abc import ABC, abstractmethod

class UserType(ABC):

	# Preconditions: The user has to have been instantiated
	# Postconditions: Sets the Type of the user
	# Side-effects: None
	# User Type(in) - Type of the use
	@abstractmethod
	def setType(self, int):
    		pass

	# Preconditions: The user has to have been instantiated
	# Postconditions: Gets the Type of the user
	# Side-effects: None
	# User Type(out) - Type of the user
	@abstractmethod
	def getType(self):
		pass