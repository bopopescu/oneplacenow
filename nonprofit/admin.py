from django.contrib import admin

# Register your models here.

from .models import BridgeClassEnroll, BridgeInstructorEnroll, Class, ClassLevel, Instructor, Student

admin.site.register(BridgeClassEnroll)
admin.site.register(BridgeInstructorEnroll)
admin.site.register(Class)
admin.site.register(ClassLevel)
admin.site.register(Instructor)
admin.site.register(Student)
