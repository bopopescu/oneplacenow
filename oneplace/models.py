from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

class Instructor(models.Model):
	instructor_alt_id = models.CharField(max_length=50, null=True, default='no instructor id')
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	address = models.CharField(max_length=50, blank=True, null=True)
	zipcode = models.CharField(max_length=10, blank=True, null=True)
	state = models.CharField(max_length=20, blank=True, null=True)
	city = models.CharField(max_length=50, blank=True, null=True)
	cell_phone = models.CharField(max_length=20, default='###-###-####', null=True)
	rate = models.DecimalField(decimal_places=2, max_digits=6, blank=True, null=True, default=0)
	instructor_picture = models.FileField(blank=True,null=True, default='default2.jpg')
    
	def __str__(self):
		return 'Instructor ID: ' + self.instructor_alt_id + ' - ' + str(self.first_name)  + ' ' + str(self.last_name)

	def get_absolute_url(self):
		return reverse('oneplace:instructor')

class Student(models.Model):
	student_alt_id = models.CharField(max_length=50, null=True, default='no student id')
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	address = models.CharField(max_length=50, blank=True, null=True)
	zipcode = models.CharField(max_length=10, blank=True, null=True)
	state = models.CharField(max_length=20, blank=True, null=True)
	city = models.CharField(max_length=50, blank=True, null=True)
	cell_phone = models.CharField(max_length=20, default='###-###-####', null=True)
	student_picture = models.FileField(blank=True,null=True, default='default2.jpg')

	def get_absolute_url(self):
		return reverse('oneplace:student')

	def __str__(self):
		return 'Student ID: ' + self.student_alt_id + ' - ' + str(self.first_name)  + ' ' + str(self.last_name)


class Lesson(models.Model):
	class_alt_id = models.CharField(max_length=50, null=True, default='no lesson id')
	class_name = models.CharField(max_length=60)
	class_description = models.TextField(max_length=500)
	class_capacity = models.IntegerField(blank=True, null=True)
	start_time = models.DateTimeField(blank=True, null=True)
	end_time = models.DateTimeField(blank=True, null=True)
	room_location = models.CharField(blank=True, null=True, max_length=30, default='TBA')
	level = models.ForeignKey('Lesson_level', on_delete=models.CASCADE, blank=True, null=True)
	student_members = models.ManyToManyField(Student, through='student_in_lesson')
	instructor_members = models.ManyToManyField(Instructor, through='instructor_in_lesson')

	def __str__(self):
         return self.class_alt_id + ' - ' + self.class_name
	
	def get_absolute_url(self):
		return reverse('oneplace:lesson')


class Lesson_level(models.Model):
    level_name = models.CharField(max_length=50)
    level_description = models.TextField(max_length=500, blank=True, null=True)
    def __str__(self):
         return self.level_name


class Student_in_lesson(models.Model):
	lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	enrollment_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)

	def __str__(self):
		return str(self.student) + ' - ' + str(self.lesson)  + ' - ' + str(self.enrollment_date)

	class Meta:
		unique_together = (('student', 'lesson'),)

	def get_absolute_url(self):
		return reverse('oneplace:lesson')

class Instructor_in_lesson(models.Model):
	lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
	instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
	enrollment_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)

	def __str__(self):
		return str(self.instructor) + ' - ' + str(self.lesson)  + ' - ' + str(self.enrollment_date)

	class Meta:
		unique_together = (('instructor', 'lesson'),)

	def get_absolute_url(self):
		return reverse('oneplace:lesson')
