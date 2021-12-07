from django.shortcuts import render, redirect
from django.views import View
from .models import UserProfile
from TAScheduler.Managment.UserManagement import UserManagement

# Create your views here.
class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        noUser = False
        incorrectPassword = False
        try:
            checkUser = UserProfile.objects.get(userName=request.POST['useraccount'])
            incorrectPassword = (checkUser.userPassword != request.POST['password'])
        except:
            noUser = True
        if noUser:
            newUser = UserProfile(userName=request.POST['useraccount'], userPassword=request.POST['password'])
            newUser.save()
            return redirect("/home/")
        elif incorrectPassword:
            return render(request, "login.html")
        else:
            return redirect("/home/")


class Home(View):
    def get(self, request):
        return render(request, "home.html", {})

class CreateUser(View):
    def get(self, request):
        return render(request, "createuser.html", {})

class ClassSchedules(View):
    pass


class UserManagement(View):
    pass


class ClassLabManagement(View):
    pass


class CourseTAAssignments(View):
    pass


class UserList(View):
    pass


class AccountCreation(View):
    pass


class ClassList(View):
    pass


class CourseCreation(View):
    pass


class LabList(View):
    pass


class CourseAssignments(View):
    pass


class TAList(View):
    pass

  
class CreateCourse(View):
    def get(self, request):
        return render(request, "createcourse.html,", {})
