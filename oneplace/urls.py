from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from oneplace import views
from . import views

app_name = 'oneplace'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^class/$', views.LessonView.as_view(), name='lesson'),
    url(r'^class/table/$', views.LessonTable, name='lesson_table'),
    #url(r'^class/table/$', views.LessonTableView.as_view(), name='lesson_table'),
    url(r'^class/add/$', views.LessonCreate.as_view(), name='lesson_add'),
    url(r'^class/update/(?P<pk>[0-9]+)/$', views.LessonUpdate.as_view(), name='lesson_update'),
    url(r'^class/delete/(?P<pk>[0-9]+)/$', views.LessonDelete.as_view(), name='lesson_delete'),
    url(r'^class/delete/(?P<pk>[0-9]+)/list/$', views.LessonDeleteList.as_view(), name='lesson_delete_list'),
    url(r'^class/calendar/$', views.calendar, name='calendar'),
    url(r'^student/$', views.StudentDisplayAll, name='student'),
    url(r'^student/add/$', views.StudentCreate.as_view(), name='student_add'),
    url(r'^student/update/(?P<pk>[0-9]+)/$', views.StudentUpdate.as_view(), name='student_update'),
    url(r'^student/delete/(?P<pk>[0-9]+)/$', views.StudentDelete.as_view(), name='student_delete'),
    url(r'^student/remove/(?P<studentpk>[0-9]+)/(?P<lessonpk>[0-9]+)$', views.StudentRemove, name='student_remove'),
    url(r'^instructor/$', views.InstructorDisplayAll, name='instructor'),
    url(r'^instructor/add/$', views.InstructorCreate.as_view(), name='instructor_add'),
    url(r'^instructor/delete/(?P<pk>[0-9]+)/$', views.InstructorDelete.as_view(), name='instructor_delete'),
    url(r'^instructor/update/(?P<pk>[0-9]+)/$', views.InstructorUpdate.as_view(), name='instructor_update'),
    url(r'^instructor/remove/(?P<instructorpk>[0-9]+)/(?P<lessonpk>[0-9]+)$', views.InstructorRemove, name='instructor_remove'),
    url(r'^student/enroll/$', views.StudentEnrollCreate.as_view(), name='student_enroll'),
    url(r'^instructor/assign/$', views.InstructorAssignCreate.as_view(), name='instructor_assign'),
    url(r'^class/enrollment/(?P<pk>[0-9]+)/$', views.ClassEnrollment, name='class_enrollment'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.logoutView, name='log_out'),
    url(r'^rest/api$', views.StudentList.as_view(), name='rest'),
    url(r'^chart/$', views.chart, name='chart'),
    url(r'^chart/charttotalstudent$', views.chart_total_student, name='chart_total_student'),
    url(r'^chart/chartclasspermonth$', views.chart_class_per_month, name='chart_class_per_month'),
    url(r'^chart/chartcapacity$', views.chart_capacity, name='chart_capacity'),
    url(r'^chart/chart_level$', views.chart_level, name='chart_level'),
    url(r'^test$', views.test, name='test'),
    
    ]

urlpatterns = format_suffix_patterns(urlpatterns)

#maybe use later
#url(r'^student/$', views.StudentView.as_view(), name='student'),
#url(r'^instructor/$', views.InstructorView.as_view(), name='instructor'),