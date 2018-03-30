from django.conf.urls import patterns,include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$','students.students.students_list',name = 'home'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^groups/$','students.students.groups_list',name='groups'),

    url(r'^students/add/$','students.students.students_add',name='students_add'),

    url(r'^students/(?P<sid>\d+)/edit/$','students.students.students_edit',name='students_edit'),

    url(r'^students/(?P<sid>\d+)/delete','students.students.students_delete',name = 'students_delete'),

   # Groups urls
    url(r'^groups/$', 'students.students.groups_list', name='groups'),

    url(r'^groups/add/$', 'students.students.groups_add',name='groups_add'),

    url(r'^groups/(?P<gid>\d+)/edit/$','students.students.groups_edit',name='groups_edit'),
                       
    url(r'^groups/(?P<gid>\d+)/delete/$','students.students.groups_delete',name='groups_delete'),
 )