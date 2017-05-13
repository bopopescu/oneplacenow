from rest_framework import serializers
from oneplace.models import Instructor, Student, Lesson, Lesson_level, Student_in_lesson, Instructor_in_lesson



class InstructorSerializer(serializers.ModelSerializer):

	class Meta:
		model = Instructor
		fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Student
		fields = '__all__'



class LessonSerializer(serializers.ModelSerializer):

	class Meta:
		model = Lesson
		fields = '__all__'

class Lesson_levelSerializer(serializers.ModelSerializer):

	class Meta:
		model = Lesson_level
		fields = '__all__'

class Student_in_lessonSerializer(serializers.ModelSerializer):

	class Meta:
		model = Student_in_lesson
		fields = '__all__'

class Instructor_in_lessonSerializer(serializers.ModelSerializer):

	class Meta:
		model = Instructor_in_lesson
		fields = '__all__'