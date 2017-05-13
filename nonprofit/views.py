from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from .models import Class, Student, ClassLevel, Instructor, BridgeInstructorEnroll, BridgeClassEnroll
from django.core.urlresolvers import reverse_lazy

def home(request):
	return render(request, 'nonprofit/index.html')

class LessonView(generic.ListView):
    template_name = 'nonprofit/class_detail.html'
    context_object_name ='all_Class'
    def get_queryset(self):
        return Class.objects.all()
        

def student(request, class_field): 
    student_List = BridgeClassEnroll.objects.filter(class_field=class_field)  
    student_Count = BridgeClassEnroll.objects.filter(class_field=class_field).count()
    lesson = Class.objects.get(pk=class_field)
    student_Info = []
    
    lessonExists = get_object_or_404(Class, pk = class_field)


    for student_pk in student_List.values():
        student_row=Student.objects.get(pk = student_pk['student_id'])
        student_Info.append(student_row)
       
    context = {'all_Student': student_List, 
               'lesson': lesson, 
               'student_Info': student_Info,
               'student_Count': student_Count } 
    return render(request, 'nonprofit/student.html', context)


def instructor_form(request):
    all_Class = Class.objects.all() 
    context = {'all_Class' : all_Class,
               }
    '''print(request.POST['last_n'])'''
    '''print(request.POST['phone_Number'])'''

    return render(request, 'nonprofit/instructor.html', context)

def instructor_add(request):
    all_Class = Class.objects.all() 
    context = {'all_Class' : all_Class,
               }
    new_instructor = Instructor()
    new_instructor.rocket_id = request.POST['rocket_id']
    new_instructor.first_name = request.POST['first_n']
    new_instructor.last_name = request.POST['last_n']
    new_instructor.address = request.POST['address']
    new_instructor.zip_code = request.POST['zip_code']
    new_instructor.state = request.POST['state']
    new_instructor.cell_phone = request.POST['phone_number']
    new_instructor.save()
    
    return render(request, 'nonprofit/instructor.html', context)

class LessonCreate(CreateView):
	model = Class
	fields = ['class_id','class_name','class_description','class_capacity', 'start_time','end_time']


class LessonUpdate(UpdateView):
    model = Class
    fields = ['class_id','class_name','class_description','class_capacity', 'start_time','end_time']

class LessonDelete(DeleteView):
    
    
    model = Class
    success_url = reverse_lazy('nonprofit:lesson')

    def get_object(self):
        student_List = BridgeClassEnroll.objects.filter(class_field=self.class_id)
        return self.model.objects.get(class_id=self.request.POST.get('class_id'))
