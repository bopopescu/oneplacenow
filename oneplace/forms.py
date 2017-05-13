from django.contrib.auth.models import User
from django import forms
from django.contrib.admin import widgets
from oneplace.models import Instructor, Student, Lesson, Lesson_level, Student_in_lesson, Instructor_in_lesson
from django.forms import ModelForm
from django.db import models


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ['username', 'email', 'password']

class LoginForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username', 'password']



class StudentForm(forms.Form):
    start_time = forms.DateField(widget=forms.DateTimeInput)


class UploadFileForm(forms.Form):
    file = forms.FileField(label='Import CSV Data', required=False)

