from django.shortcuts import render, redirect
from django.views import View
from .models import UserProfile, Course, Lab
<<<<<<< Updated upstream
from TAScheduler.Managment.UserManagement import UserManagement

=======
>>>>>>> Stashed changes

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
            # following line will need to be replaced once createUser method working
            checkUser = UserProfile(userName=request.POST['useraccount'], userPassword=request.POST['password'],
                                    userType="TA")
            checkUser.save()
            return redirect("/home/")
        elif incorrectPassword:
            return render(request, "login.html")
        else:
            request.session["name"] = checkUser.userName
            return redirect("/home/")


class Home(View):
    def get(self, request):
        return render(request, "home.html", {})


class CreateUser(View):
    def get(self, request):
        if UserProfile.objects.get(userName=request.session["name"]).userType == "SUPERVISOR":
            return render(request, "createuser.html", {})
        else:
            return redirect("/../home/")

    def post(self, request):
        newUser = UserProfile(userID=request.POST['userID'], userType=request.POST['userType'].upper(),
                              userPassword=request.POST['userPassword'], userName=request.POST['userName'],
                              userAddress=request.POST['userAddress'], userContact=request.POST['userContact'],
                              userEmail=request.POST['userEmail'])
        newUser.save()
        return render(request, "createuser.html")


class CreateCourse(View):
    def get(self, request):
        if UserProfile.objects.get(userName=request.session["name"]).userType == "SUPERVISOR":
            return render(request, "createcourse.html", {})
        else:
            return redirect("/../home/")

    def post(self, request):
        newCourse = Course(courseID=request.POST['ID'], name=request.POST['name'], location=request.POST['location'],
                           hours=request.POST['hours'], days=request.POST['days'],
                           instructor=UserProfile.objects.get(userName=request.POST['instructor']))
        newCourse.save()
        newCourse.TAs.add(UserProfile.objects.get(userName=request.POST['TAs']))
        newCourse.labs.add(Lab.objects.get(name=request.POST['labs']))
        newCourse.save()
        return render(request, "createcourse.html")


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
