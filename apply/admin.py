from django.contrib import admin

from .models import Source, Academic, Course, Department, Subject_code, Major, Grade, Choice, User_apply_profile, UserPriorChoice

admin.site.register(Source)
admin.site.register(Academic)
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Subject_code)
admin.site.register(Major)
admin.site.register(Choice)
admin.site.register(User_apply_profile)
admin.site.register(UserPriorChoice)
