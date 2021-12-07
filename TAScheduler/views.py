from django.shortcuts import render
from django.views import View
from classses import Instructor,

# Create your views here.
class Login(View):
    def get(self, request):
        return render(request, "login.html", {})

class Home(View):
    def get(self, request):
        return render(request, "home.html", {})

class CreateUser(View):
    def get(self, request):
        return render(request, "createuser.html", {})

class CreateCourse(View):
    def get(self, request):
        return render(request, "createcourse.html,", {})