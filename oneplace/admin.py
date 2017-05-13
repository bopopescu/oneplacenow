from django.contrib import admin
# Register your models here.
from oneplace.models import Instructor, Student, Lesson, Lesson_level, Student_in_lesson, Instructor_in_lesson

admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(Lesson)
admin.site.register(Lesson_level)
admin.site.register(Student_in_lesson)
admin.site.register(Instructor_in_lesson)