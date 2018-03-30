# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

def journal_list(request):
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
    return render(request, 'students/journal.html', {'students': students})
