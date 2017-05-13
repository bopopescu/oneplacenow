from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from oneplace.models import Instructor, Student, Lesson, Lesson_level, Student_in_lesson, Instructor_in_lesson
from django.urls import reverse_lazy
from .forms import UserForm, LoginForm, StudentForm, UploadFileForm
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from oneplace.serializers import StudentSerializer
import time, csv, datetime
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.core.files.uploadedfile import UploadedFile,  TemporaryUploadedFile
from io import TextIOWrapper


# Create your views here.
def index(request):

    return render(request, 'oneplace/index.html')

def logoutView(request):
    logout(request)
    return redirect('oneplace:index')

class LessonView(generic.ListView):
    template_name = 'oneplace/lesson.html'
    context_object_name ='lesson_all'
    def get_queryset(self):
        return Lesson.objects.all().order_by('start_time')

class LessonTableView(generic.ListView):
    template_name = 'oneplace/lessontable.html'
    context_object_name ='lesson_all'
    def get_queryset(self):
        return Lesson.objects.all().order_by('start_time')

def test(request):
    class_bulk_data = []
    
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        
        if form.is_valid():
          class_bulk_data  = handle_uploaded_file(request.FILES['file'].file, request)
          
          count_Save = 0
          for idx, row in enumerate(class_bulk_data):
              if idx > 0:
                  get_Level = Lesson_level.objects.get(level_name=class_bulk_data[idx][6])
                  new_Class_Entry = Lesson(class_name = class_bulk_data[idx][0], 
                                       class_description = class_bulk_data[idx][1], 
                                       class_capacity = class_bulk_data[idx][2],
                                       start_time = class_bulk_data[idx][3], 
                                       end_time = class_bulk_data[idx][4],
                                       room_location = class_bulk_data[idx][5],
                                       level = get_Level
                                       )
                  new_Class_Entry.save()
                  print (get_Level)
                  count_Save+=1
        print("You Saved:" + str(count_Save))
            
    else:
        form = UploadFileForm()
        

    return render(request, 'oneplace/test.html', {'form':form})

def handle_uploaded_file(f, request):
    class_bulk_data = []
    
    f=TextIOWrapper(request.FILES['file'].file, encoding=request.encoding)
    file_reader = csv.reader(f, delimiter=',', skipinitialspace=True)
    
    for row in file_reader:
        class_bulk_data.append(row)
    
    return class_bulk_data

def LessonTable(request):

    lesson_all = Lesson.objects.all().order_by('start_time')
    
    if request.method == 'POST':
        #Search Function

        search_value = request.POST.get("search")
        if search_value is not None:
            lesson_all = Lesson.objects.filter(class_name__icontains=search_value)
        
        #for Bulk upload
        form = UploadFileForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            class_bulk_data  = handle_uploaded_file(request.FILES['file'].file, request)
          
            count_Save = 0
            for idx, row in enumerate(class_bulk_data):
                if idx > 0:
                    get_Level = Lesson_level.objects.get(level_name=class_bulk_data[idx][6])
                    new_Class_Entry = Lesson(class_name = class_bulk_data[idx][0], 
                                       class_description = class_bulk_data[idx][1], 
                                       class_capacity = class_bulk_data[idx][2],
                                       start_time = class_bulk_data[idx][3], 
                                       end_time = class_bulk_data[idx][4],
                                       room_location = class_bulk_data[idx][5],
                                       level = get_Level
                                       )
                    new_Class_Entry.save()
                    print (get_Level)
                    count_Save+=1
        print("You Saved:" + str(count_Save))
    else:
        form = UploadFileForm()
      
    context = {'lesson_all': lesson_all,
               'form': form, 
               }
               
    return render(request, 'oneplace/lessontable.html', context)

#does not update the count
class StudentView(generic.ListView):
    template_name = 'oneplace/student.html'
    context_object_name ='student_Info'
    
    studentCount = Student.objects.all().count()

    
    def get_queryset(self):
        return Student.objects.all()

    def get_context_data(self, **kwargs):
        context = super(StudentView, self).get_context_data(**kwargs)
        context.update({'studentCount': self.studentCount})
        return context

def StudentDisplayAll (request):
    student_Info = Student.objects.all().order_by('-student_picture')
    studentCount = Student.objects.all().count()
    context = {'student_Info': student_Info, 
               'studentCount': studentCount}
               
    return render(request, 'oneplace/student.html' , context)


class LessonCreate(CreateView):
	model = Lesson
	fields = ['class_name','class_description','class_capacity', 'start_time','end_time', 'level', 'room_location']


class LessonUpdate(UpdateView):
	model = Lesson
	fields = ['class_name','class_description','class_capacity', 'start_time','end_time', 'room_location', 'level']


class StudentCreate(CreateView):
	model = Student
	fields = ['first_name', 'last_name', 'address', 'state', 'city', 'zipcode', 'cell_phone', 'student_picture']


class StudentUpdate(UpdateView):
	model = Student
	fields = ['first_name', 'last_name', 'address', 'state', 'city', 'zipcode', 'cell_phone', 'student_picture']


class StudentDelete(DeleteView):
	model = Student
	fields = ['first_name', 'last_name', 'address', 'state', 'city', 'zipcode', 'cell_phone', 'student_picture']	
	success_url = reverse_lazy('oneplace:student')

#count does not update corrects so the view below is not in use
class InstructorView(generic.ListView):
    template_name = 'oneplace/instructor.html'
    context_object_name ='instructor_Info'
    
    instructorCount = Instructor.objects.all().count()

    
    def get_queryset(self):
        return Instructor.objects.all()

    def get_context_data(self, **kwargs):
        context = super(InstructorView, self).get_context_data(**kwargs)
        context.update({'instructorCount': self.instructorCount})
        return context
    
def InstructorDisplayAll (request):
    instructor_Info = Instructor.objects.all().order_by('-instructor_picture')
    instructorCount = Instructor.objects.all().count()
    context = {'instructor_Info': instructor_Info, 
               'instructorCount': instructorCount}
               
    return render(request, 'oneplace/instructor.html' , context)
        

class InstructorCreate(CreateView):
	model = Instructor
	fields = ['first_name', 'last_name', 'address','state', 'city', 'zipcode', 'cell_phone', 'rate', 'instructor_picture']


class InstructorUpdate(UpdateView):
	model = Instructor
	fields = ['first_name', 'last_name', 'address', 'state', 'city', 'zipcode', 'cell_phone', 'rate', 'instructor_picture']


class InstructorDelete(DeleteView):
	model = Instructor
	fields = ['first_name', 'last_name', 'address', 'state', 'city', 'zipcode', 'cell_phone','rate', 'instructor_picture']	
	success_url = reverse_lazy('oneplace:instructor')


class StudentEnrollCreate(CreateView):
	model = Student_in_lesson
	fields = ['lesson','student']

#def StudentEnrollDash(request, class_id)

    #return render(request, 'oneplace/class_enrollment.html', context)



class InstructorAssignCreate(CreateView):
	model = Instructor_in_lesson
	fields = [ 'lesson', 'instructor']


class LessonDelete(DeleteView):    
    model = Lesson
    success_url = reverse_lazy('oneplace:lesson')

class LessonDeleteList(DeleteView):    
    model = Lesson
    success_url = reverse_lazy('oneplace:lesson_table')

def ClassEnrollment(request, pk): 
    lesson = Lesson.objects.get(pk=pk)
    student_in_lesson = lesson.student_members.all()
    instructor_assign_lesson = lesson.instructor_members.all()
    student_Count = lesson.student_members.all().count()
    context = {'lesson': lesson, 
               'student_Info': student_in_lesson, 
               'instructor_Info': instructor_assign_lesson,
               'student_Count': student_Count } 
    return render(request, 'oneplace/class_enrollment.html', context)


def StudentRemove(request, studentpk, lessonpk):
	student_delete=Student_in_lesson.objects.get(student=studentpk, lesson=lessonpk)
	student_delete.delete()
	return ClassEnrollment(request, lessonpk)

def InstructorRemove(request, instructorpk, lessonpk):
    instructor_delete=Instructor_in_lesson.objects.get(instructor=instructorpk, lesson=lessonpk)
    instructor_delete.delete()
    return ClassEnrollment(request, lessonpk)

class UserFormView(View):
    form_class = UserForm
    template_name = 'oneplace/registration_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

#process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            #cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user.set_password(password)
            user.save()

            #returns User object if credentials are correct
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # request.user.username or request.user.user
                    return redirect('oneplace:index')
        return render(request, self.template_name, {'form':form})

class LoginFormView(View):
    form_class = LoginForm
    template_name = 'oneplace/login_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

#process form data
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        print (user)
            #returns User object if credentials are correct
        if user is not None:
            if user.is_active:
                login(request, user)
                # request.user.username or request.user.user
                return redirect('oneplace:index')
        else:
            #invalid Login
            print ("invalid login details:" + username + " " + password)
            login_Error = True
            form = self.form_class(None)
            return render(request, self.template_name, {'form':form, 'login_Error':login_Error})
        

#REST
class StudentList(APIView):

    def get(self,request):
        student=Student.objects.all()
        serializer=StudentSerializer(student, many=True)
        return Response(serializer.data)

    def post(self):
        pass


def chart(request):
    lesson = Lesson.objects.all().order_by('start_time')[:10]
    lessonName = []
    lessonStudentCount = []
    lessonMaxEnrollment = []
    lessonTotalMonth = [i * 0 for i in range (12)]

    
    lessonPerMonth = Lesson.objects.annotate(month=TruncMonth('start_time')).values('month').annotate(numClass=Count('id')) 
    levelCount = Lesson.objects.values('level').annotate(levelcount=Count('level')).values('level__level_name','levelcount')
     
    for value in lessonPerMonth:
        #print (value)
        #print(value['month'].month, value['numClass'])
        if value['month'].month > 0 and value['month'].month <= 12:
            lessonTotalMonth[value['month'].month -1] = value['numClass']
   
    for value in lesson:
        lessonName.append(value.class_name)
        if value.class_capacity is None:
            lessonMaxEnrollment.append('0')
        else:
            lessonMaxEnrollment.append(value.class_capacity)

        lessonStudentCount.append(Student_in_lesson.objects.filter(lesson = value.pk).count())

    context = {'lessonName':lessonName,
               'lessonStudentCount': lessonStudentCount,
               'lessonTotalMonth':lessonTotalMonth,
               'lessonMaxEnrollment':lessonMaxEnrollment,
               'levelCount':levelCount
    }
    
    return render(request, 'oneplace/charts.html' , context)


def chart_total_student(request):
    lesson = Lesson.objects.all().order_by('start_time')[:10]
    lessonName = []
    lessonStudentCount = []

    for value in lesson:
        lessonName.append(value.class_name)
        lessonStudentCount.append(Student_in_lesson.objects.filter(lesson = value.pk).count())

    context = {'lessonName':lessonName,
                 'lessonStudentCount': lessonStudentCount
    }
    return render(request, 'oneplace/charts_total_student.html' , context)

def chart_class_per_month(request):
    lesson = Lesson.objects.all().order_by('start_time')[:10]
    lessonTotalMonth = [i * 0 for i in range (12)]
 
    lessonPerMonth = Lesson.objects.annotate(month=TruncMonth('start_time')).values('month').annotate(numClass=Count('id')) 
   
     
    for value in lessonPerMonth:
      
        if value['month'].month > 0 and value['month'].month <= 12:
            lessonTotalMonth[value['month'].month -1] = value['numClass']

    context = {'lessonTotalMonth':lessonTotalMonth,
           
    }
    
    return render(request, 'oneplace/charts_class_per_month.html' , context)


def chart_capacity(request):
    lesson = Lesson.objects.all().order_by('start_time')[:10]
    lessonName = []
    lessonStudentCount = []
    lessonMaxEnrollment = []

    for value in lesson:
        if value.class_capacity is not None:
            #print(value.class_capacity)
            lessonName.append(value.class_name)
            lessonMaxEnrollment.append(value.class_capacity)
            lessonStudentCount.append(Student_in_lesson.objects.filter(lesson = value.pk).count())

    context = {'lessonName':lessonName,
               'lessonStudentCount': lessonStudentCount,
               'lessonMaxEnrollment':lessonMaxEnrollment,
    }
    
    return render(request, 'oneplace/charts_capacity.html' , context)

def chart_level(request):
    lesson = Lesson.objects.all().order_by('start_time')[:10]
    levelCount = Lesson.objects.values('level').annotate(levelcount=Count('level')).values('level__level_name','levelcount')

    context = {'levelCount':levelCount}

    return render(request, 'oneplace/charts_level.html' , context)


def calendar(request):
    calendarInfo = Lesson.objects.all().order_by('start_time')
    now = str(datetime.datetime.now().strftime("%Y-%m-%d"))
    formatted = {}
    list_final =[]

    for value in calendarInfo:
       start_time = str(value.start_time).replace(" ", "T",1)
       end_time = str(value.end_time).replace(" ", "T",1)
       lesson_id = value.id

       formatted['id']= value.id
       formatted['title'] = value.class_name
       formatted['start'] = start_time
       formatted['end'] = end_time

       list_final.append(formatted.copy())

    context = {'calendarInfo': list_final,
                'now':now
                }

    return render(request, 'oneplace/calendar.html', context)


def search_class(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StudentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return

    # if a GET (or any other method) we'll create a blank form
    else:
        form = StudentForm()

    return render(request, 'oneplace/test.html', {'form': form})




