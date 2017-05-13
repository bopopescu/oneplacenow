from django.conf.urls import url

from . import views

app_name = 'nonprofit'

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^class/$', views.LessonView.as_view(), name='lesson'),
    url(r'^class/(?P<class_field>[C][0-9]+)/$', views.student, name='student'),
    url(r'^instructor/form/$', views.instructor_form, name='instructor_form'),
    url(r'^instructor/add/$', views.instructor_add, name='instructor_add'),
    url(r'^class/add/$', views.LessonCreate.as_view(), name='lesson_add'),
    url(r'^class/update/(?P<pk>[C][0-9]+)/$', views.LessonUpdate.as_view(), name='lesson_update'),
    url(r'^class/delete/(?P<pk>[C][0-9]+)/$', views.LessonDelete.as_view(), name='lesson_delete')
    
]

'''url(r'^$', views.index, name='index'),
    url(r'^(?P<class_field>[C][0-9]+)/$', views.student, name='student'),
    url(r'^(?P<pk>[C][0-9]+)/$', views.StudentView.as_view(), name='student'),
    '''