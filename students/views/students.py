# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from ..models.group import Group
from ..models.student import Student
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.core.urlresolvers import reverse
from datetime import datetime
import os

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
        # Якщо кнопка Додати була натиснута:
        if request.POST.get('add_button') is not None:
            errors = {}
            data = {"middle_name":request.POST.get("middle_name"),
                    "notes": request.POST.get("notes")}


            # ВАЛІДАЦІЯ ДАНИХ
            first_name = request.POST.get("first_name", '').strip()
            if not first_name:
                errors["first_name"] = "Це поле мусить бути заповненим!"
            else:
                data["first_name"] = first_name
            last_name = request.POST.get("last_name", "").strip()
            if not last_name:
                errors["last_name"] = "Це поле мусить бути запоаненим!"
            else:
                data["last_name"] = last_name
            birthday= request.POST.get("birthday","").strip()
            if not birthday:
                errors["birthday"] = "Це поле мусить бути заповненим"
            else :
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors["birthday"] = "Введіть коректний формат дати РР-ММ-ДД"
                else:
                    data["birthday"]= birthday

            ticket = request.POST.get("ticket", "").strip()
            if not ticket:
                errors["ticket"] = "Це поле мусить бути заповненим"
            else:
                data["ticket"] = ticket

            student_group = request.POST.get("student_group","")
            if not student_group:
                errors["group"] = "Виберіть будь ласка групу"
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups)!=1:
                    errors["group"] = "Оберіть коректну групу"
                else:
                    data['student_group'] = groups[0]
            photo = request.FILES.get("photo")
            if photo:
                photo_extention = str(photo)
                photo_extention = photo_extention.split('.')[1]
                if photo_extention in ['png','jpg']:
                    data["photo"] = photo
                else: errors["photo"] = "Розширення фалу не підтримується"
            if not errors:
                student = Student(**data)
                student.save()
                student_name_for_status_message = data["last_name"] + ' '+ data["first_name"]
                return HttpResponseRedirect( u'%s?status_message=Студент %s успішно доданий!'%(reverse('home'),student_name_for_status_message))
            else: # Якщо дані були введені некоректно:
                    # Віддаємо шаблон форми разом із знайденими помилками
                return  render(request,'students/student_add.html',{"groups":Group.objects.all().order_by('title'),
                                                          "errors":errors})
        # Якщо кнопка Скасувати була натиснута:
        elif request.POST.get('cancel_button') is not None:
            # Повертаємо користувача до списку студентів
            return HttpResponseRedirect(u'%s?status_message=Додавання скасовано'%reverse('home'))

    else:
        return render(request,'students/student_add.html',{"groups":Group.objects.all().order_by('title')})





    # Якщо форма не була запощена:

        # повертаємо код початкового стану форми
def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
