# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from ..models.group import Group
from ..models.student import Student
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.core.urlresolvers import reverse

def students_list(request):
    students = Student.objects.all()
    if request.get_full_path() == "/":  ### код який автоматично загружає сторінку з фільтром
        # redirect request.GET on its copy(deep copy) which I will amend    ### але не міняє самої урли
        request.GET = request.GET.copy()
        # assign 'order_by' value 'last_name'
        request.GET.__setitem__('order_by', 'last_name')
        ### заврешення
    order_by = request.GET.get('order_by', '')  ### початок сортування по колонках
    if order_by in ('last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', ''):
            students = students.reverse()

    # PAGINATOR
    paginator = Paginator(students, 3)
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
    # Якщо форма була запощена:
    if request.method == 'POST':
        # Якщо кнопка Скасувати була натиснута:
             # Повертаємо користувача до списку студентів
        # Якщо кнопка Додати була натиснута:
        if request.POST.get('add_button') is not None:
            errors = {}
            if not errors:
                student = Student(

                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    middle_name=request.POST['middle_name'],
                    birthday=request.POST['birthday'],
                    ticket=request.POST['ticket'],
                    student_group=Group.objects.get(pk=request.POST['student_group']),
                    photo=request.FILES["photo"]
                )
                student.save()
                return HttpResponseRedirect(reverse('home'))
            else:
                return  render(request,'students/student_add.html',{"groups":Group.objects.all().order_by('title'),
                                                                    "errors":errors})
        elif request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect(reverse('home'))

    else:
        return render(request,'students/student_add.html',{"groups":Group.objects.all().order_by('title')})
            # Перевіряємо дані на коректність та збираємо помилки


                # Якщо дані були введені некоректно:

                    # Віддаємо шаблон форми разом із знайденими помилками


                # Якщо дані були введені коректно:

                # Створюємо та зберігаємо студента в базу


                # Повертаємо користувача до списку студентів


    # Якщо форма не була запощена:

        # повертаємо код початкового стану форми
def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
