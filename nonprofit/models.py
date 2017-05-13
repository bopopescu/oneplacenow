# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse


class BridgeClassEnroll(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    class_field = models.ForeignKey('Class', models.DO_NOTHING, db_column='class_id')  # Field renamed because it was a Python reserved word.
    student = models.ForeignKey('Student', models.DO_NOTHING)
    enrollment_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
         return str(self.class_field) + ' - ' + str(self.student)  + ' - ' + str(self.enrollment_date)

    class Meta:
        db_table = 'django_bridge_class_enroll'
        unique_together = (('student', 'class_field'),)


class BridgeInstructorEnroll(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    class_field = models.ForeignKey('Class', models.DO_NOTHING, db_column='class_id')  # Field renamed because it was a Python reserved word.
    rocket = models.ForeignKey('Instructor', models.DO_NOTHING)
    assignment_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
         return str(self.class_field) + ' - ' + str(self.rocket)  + ' - ' + str(self.assignment_date)

    class Meta:
        db_table = 'django_bridge_instructor_enroll'
        unique_together = (('rocket', 'class_field'),)


class Class(models.Model):
    class_id = models.CharField(primary_key=True, max_length=20)
    class_name = models.CharField(max_length=50)
    class_description = models.CharField(max_length=500)
    class_capacity = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    level = models.ForeignKey('ClassLevel', models.DO_NOTHING, blank=True, null=True)
    def __str__(self):
         return self.class_id + ' - ' + self.class_name
    

    def get_absolute_url(self):
        return reverse('nonprofit:lesson')

    class Meta:
        db_table = 'django_class'


class ClassLevel(models.Model):
    level_id = models.CharField(primary_key=True, max_length=20)
    level_name = models.CharField(max_length=50)
    level_description = models.CharField(max_length=250, blank=True, null=True)
    def __str__(self):
         return self.level_id + ' - ' + self.level_name

    class Meta:
        db_table = 'django_class_level'

class Instructor(models.Model):
    rocket_id = models.CharField(primary_key=True, max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    cell_phone = models.CharField(max_length=20)
	
    def __str__(self):
         return self.rocket_id + ' - ' + self.first_name + ' ' + self.last_name
    
    def get_absolute_url(self):
        return reverse('nonprofit/lesson')

    class Meta:
        db_table = 'django_instructor'


class Student(models.Model):
    student_id = models.CharField(primary_key=True, max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    cell_phone = models.CharField(max_length=20)
    student_picture = models.FileField(null=True)
    
    def __str__(self):
         return 'Student ID: ' + self.student_id + ' - ' + str(self.first_name)  + ' ' + str(self.last_name)

    class Meta:
        db_table = 'django_student'
