from django.db import models


# Create your models here.


# UserProfile acts as the class that will be used for all users with the userType variable determining whether they
# are an instructor, TA, or Administrator
class UserProfile(models.Model):
    userID = models.IntegerField()
    userType = models.CharField(max_length=20)
    userPassword = models.CharField(max_length=20)
    userName = models.CharField(max_length=20)
    userAddress = models.CharField(max_length=20)
    userContact = models.IntegerField()
    userEmail = models.CharField(max_length=20)


# The Lab class keeps track of the information for a particular lab section and references the instructor of the course
# to keep track of which course it relates to.
class Lab(models.Model):
    labID = models.IntegerField()
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    hours = models.CharField(max_length=20)
    days = models.CharField(max_length=20)
    instructor = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    TA = models.ForeignKey(UserProfile, on_delete=models.PROTECT, related_name="TAToLab")


# The Course class keeps track of lecture sections and stores the TAs, instructors, and labs associated with it.
class Course(models.Model):
    courseID = models.IntegerField()
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    hours = models.TimeField()
    days = models.CharField(max_length=20)
    instructor = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    TAs = models.ManyToManyField(UserProfile, related_name="TAToCourse")
    labs = models.ManyToManyField(Lab)


# Schedule is a tool to be used by users to display the events they have going on in a week, be that Labs or courses.
class Schedule(models.Model):
    userID = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)
    labs = models.ManyToManyField(Lab)
