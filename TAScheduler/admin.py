from django.contrib import admin
from TAScheduler.models import UserProfile, Course, Lab, Schedule

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Course)
admin.site.register(Lab)
admin.site.register(Schedule)

