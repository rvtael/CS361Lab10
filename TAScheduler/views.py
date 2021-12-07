from django.shortcuts import render
from django.views import View


# Create your views here.
class Login(View):
    def get(self, request):
        return render(request, "login.html", {})

class Home(View):
    def get(self, request):
        return render(request, "home.html", {})


class Login(View):

class Home(View):

class ClassSchedules(View):

class UserManagement(View):

class ClassLabManagement(View):

class CourseTAAssignments(View):

class UserList(View):

class AccountCreation(View):

class ClassList(View):

class CourseCreation(View):

class LabList(View):

class CourseAssignments(View):

class TAList(View):