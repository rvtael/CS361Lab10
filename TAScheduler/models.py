from django.db import models


class User(models.Model):
    userID = models.CharField(max_length=20)
    userName = models.CharField(max_length=20)
    userContact = models.IntegerField
    userSSN = models.IntegerField
    userAddress = models.CharField(max_length=20)
    userPassword = models.CharField(max_length=20)
    userType = models.CharField(max_length=20)


class Course(models.Model):
    courseName = models.CharField(max_length=20)
    courseTime = models.CharField(max_length=20)
    courseDays = models.CharField(max_length=20)
    courseHours = models.CharField(max_length=20)
    courseInstructor = models.ForeignKey(User, on_delete=models.PROTECT)
    courseTA = models.ForeignKey(User, on_delete=models.PROTECT)


class Lab(models.Model):
    labName = models.CharField(max_length=20)
    labDays = models.CharField(max_length=20)
    labHours = models.CharField(max_length=20)
    labLocation = models.CharField(max_length=20)
    labTA = models.ForeignKey(User, on_delete=models.PROTECT)


class Assignment(models.Model):
    assignmentName = models.CharField(max_length=20)
    assignmentDue = models.DateTimeField
    assignmentDetails = models.TextField
