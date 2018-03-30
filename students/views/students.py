# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

def students_list(request):
    students = (
        {
            'id':1,
            'first_name':u'Yura',
            'last_name': u'Dudar',
            'ticket' : 11350161,
            'image':'img/1.png'
        },
        {
        'id': 2,
        'first_name': u'Корост',
        'last_name': u'Андрій',
        'ticket': 2123,
        'image': 'img/2.png'
        },
        {
        'id': 2,
        'first_name': u'Корост',
        'last_name': u'Андрій',
        'ticket': 2123,
        'image': 'img/2.png'
        },
    )
    return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)


