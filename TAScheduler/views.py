from django.shortcuts import render
from django.views import View


# Create your views here.
class Login(View):
    def get(self, request):
        return render(request, "login.html", {})

'''
Skeleton for "possible" methods needed

 --Redirect methods--

 homepage_redir()
 classSchedules_redir()
 userMgmt_redir()
 classLabManagement_redir()
 accountSettings_redir()
 courseTAAssignments_redir()
 
 
 --Subpages--
 
 userList_redir()
 accCreation_redir()
 classList_redir()
 courseCreation_redir()
 labList_redir()
 courseAssignments_redir()
 TAList_redir()
 
 --errors--
 
 
'''