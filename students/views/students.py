# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from  ..models import Student
from django.core.paginator import PageNotAnInteger,EmptyPage,Paginator
def students_list(request):
    students = Student.objects.all()
    if request.get_full_path() == "/":                                      ### код який автоматично загружає сторінку з фільтром
        # redirect request.GET on its copy(deep copy) which I will amend    ### але не міняє самої урли
        request.GET = request.GET.copy()
        # assign 'order_by' value 'last_name'
        request.GET.__setitem__('order_by', 'last_name')
        ### заврешення
    order_by = request.GET.get('order_by','')                               ### початок сортування по колонках
    if order_by in ('last_name','first_name','ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse',''):
            students = students.reverse()

    # PAGINATOR
    paginator = Paginator(students,3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)

    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver
        # last page of results.
        students = paginator.page(paginator.num_pages)

    return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)


