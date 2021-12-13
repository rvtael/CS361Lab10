
from django.db import models
from TAScheduler.models import Lab
from TAScheduler.models import UserProfile
from django.shortcuts import render

class LabManagement(object):


# class Lab(models.Model):
#    labID = models.IntegerField(default=0)
#    name = models.CharField(max_length=20)
#    location = models.CharField(max_length=20)
#    hours = models.CharField(max_length=20)
#    days = models.CharField(max_length=20)
#    instructor = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
#    TA = models.ForeignKey(UserProfile, on_delete=models.PROTECT, related_name="TAToLab")
	# Preconditions: The user has to have been instantiated.

    # Side-effects: Lab is created and added inside the database
    #Lab ID(in) - Id of the lab
    # Lab Name(in) - Name of the lab
    # Lab Hours(in) - Hours of the lab
    # Lab Location(in) - Location of the lab
    # Lab Days(in) - Days of the lab
    # Lab Instructor(in) - Instructor of the lab
    # Lab TA(in) -TA of the lab
    def createLab(request, Id, labName, labLocation, labHours, labDays, labInstructor, labTA):
        if(not(isinstance(Id, int))):
            raise TypeError("Id entered is not of type int")
        if(not(isinstance(labName, str))):
            raise TypeError("Lab Name entered is not of type str")
        if(not(isinstance(labLocation, str))):
            raise TypeError("Lab Location entered is not of type str")
        if(not(isinstance(labHours, str))):
            raise TypeError("Lab Hours entered is not of type str")
        if(not(isinstance(labDays, str))):
            raise TypeError("Lab Days entered is not of type str")
        if(not(isinstance(labInstructor, UserProfile))):
            raise TypeError("Lab Instructor entered is not of type User")
        if(labInstructor.userType != "INSTRUCTOR"):
            raise TypeError("Lab Instructor's type is not of type INSTRUCTOR")
        if (not(isinstance(labTA, UserProfile))):
            raise TypeError("Lab TA entered is not of type User")
        if(labTA.userType != "TA"):
            raise TypeError("Lab TA's type is not of type TA")

        newLab = Lab.objects.create(labID=Id, name=labName, location=labLocation, 
        hours=labHours, days=labDays, instructor=labInstructor, TA=labTA)
        newLab.save()

        return "Lab was created"

    # Side-effects: Lab is edited inside the database
    # Lab ID(in) - Id of the lab
    # Lab Name(in) - Name of the lab
    # Lab Hours(in) - Hours of the lab
    # Lab Location(in) - Location of the lab
    # Lab Days(in) - Days of the lab
    # Lab Instructor(in) - Instructor of the lab
    # Lab TA(in) -TA of the lab
    def editLab(request, Id, labName, labHours, labLocation, labDays, labInstructor, labTA):
        if(not(isinstance(Id, int))):
            raise TypeError("Id entered is not of type int")
        if(not(isinstance(labName, str))):
            raise TypeError("Lab Name entered is not of type str")
        if(not(isinstance(labLocation, str))):
            raise TypeError("Lab Location entered is not of type str")
        if(not(isinstance(labHours, str))):
            raise TypeError("Lab Hours entered is not of type str")
        if(not(isinstance(labDays, str))):
            raise TypeError("Lab Days entered is not of type str")
        if(not(isinstance(labInstructor, UserProfile))):
            raise TypeError("Lab Instructor entered is not of type User")
        if(labInstructor.userType != "INSTRUCTOR"):
            raise TypeError("Lab Instructor's type is not of type INSTRUCTOR")
        if (not(isinstance(labTA, UserProfile))):
            raise TypeError("Lab TA entered is not of type User")
        if(labTA.userType != "TA"):
            raise TypeError("Lab TA's type is not of type TA")
        
        if(not(Lab.objects.filter(labId = Id).exists())):
            return "This Lab does not exist"

        edittedLab = Lab.objects.get(labId = Id)
        
        edittedLab.name = labName
        edittedLab.location = labLocation
        edittedLab.hours = labHours
        edittedLab.days = labDays
        edittedLab.instructor = labInstructor
        edittedLab.TA = labTA

        return "The lab was successfully editted"

    # Preconditions: The user has to have been instantiated.
    # The user must be of type administrator
    # Postconditions:Deletes a lab
	  # Side-effects: Lab is deleted and removed from the database
	  # Lab Name(in) - Name of the course
    def deleteLab(request, Id):
        if(not(isinstance(Id, int))):
            raise TypeError("Id entered is not of type int")

        retMsg = "Lab has been successfully deleted"
        if(not(Lab.objects.filter(labId = Id).exists())):
            retMsg = "This lab being deleted does not exist"
        else:
            Lab.objects.filter(labId = Id).delete()

        return retMsg
        

    # Preconditions: The user has to have been instantiated
    # The LabID is an existing lab Id 
    # Postconditions: Lab assignments are populated
    # Side-effects: None
    # Lab Id(in): Lab Id you are searching for
    def populateSearchLab(request, Id):
        if(not(isinstance(Id, int))):
            raise TypeError("Id entered is not of type int")
        
        retMsg = ""
        if(not(Lab.objects.filter(labId = Id).exists())):
            retMsg = "This lab being deleted does not exist"
        else:
            retMsg = {
                'Found Lab': Lab.objects.get(labId = Id)
            }

        return retMsg
        

    # Preconditions: The user has to have been instantiated
    # There are labs to display
    # Postconditions: All labs are displayed
    # Side-effects: None
    def displayAllLabs(request):
        allLabs = Lab.objects.all()

        data = {
            'All Labs': allLabs
        }
        
        return allLabs
