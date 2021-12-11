from django.shortcuts import render, redirect
from django.views import View
from TAScheduler.models import UserProfile
from django.db import connection

# userID = models.IntegerField(default=0)
# userType = models.CharField(max_length=20, choices=[('SUPERVISOR', 'Supervisor'), ('INSTRUCTOR', 'Instructor'), ('TA', 'TA')])
# userPassword = models.CharField(max_length=20)
# userName = models.CharField(max_length=20)
# userAddress = models.CharField(max_length=20)
# userContact = models.IntegerField(default=0)
# userEmail = models.CharField(max_length=20)

#Not going to use  SSN number, going to be using the e-mail
#make sure to update all method parameters to new database standards from tonight's meeting on Friday

#comment to test pull request

class userManagement:

    def populateList(request):

        allUsers = UserProfile.objects.all()

        data={
            'allUsers':allUsers
        }

        #Place holder name for the .html file, not sure what we'll call the search feature .html file
        return render(request, "populateusers.html", data)

    def createUser(request, userID, userName, userContact, userEmail, userAddress, userPassword, userType):

        #Can also do this as 'UserProfile.objects.create(userID, userName, userContact, userSSN, userAddress, userPassword, userType)' I believe?
        # newUser = UserProfile(userID, userName, userContact, userSSN, userAddress, userPassword, userType)
        newUser = UserProfile.objects.create(userID, userName, userContact, userEmail, userAddress, userPassword, userType)
        newUser.save()
        return render(request, "createuser.html", {})

    def deleteUser(request, userID):

        if UserProfile.objects.filter(userID=userID).exists():
            UserProfile.objects.filter(userID=userID).delete()
            return render(request, "deleteuser.html", {})

    def findUser(request, userID):

        if UserProfile.objects.filter(userID=userID, userName=userName, userSSN=userSSN).exists():

            data={
                'foundUser':UserProfile.objects.get(userID=userID, userName=userName, userSSN=userSSN)
            }

            return render(request, "finduser.html", data)
        else:

            data={
                "User not found"
            }

            return render(request, "finduser.html", data)

    def editUser(request, userID, userName, userContact, , userAddress, userPassword, userType):
        #make sure to include userType checking regarding information editing
        #one method to edit a user is to delete and recreate the same user. May be issues with foreign keys - shoot email to Apoorv
