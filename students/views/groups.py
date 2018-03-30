# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

# Views for Groups
def groups_list(request):
    groups = (
        {
            'name': u'Пм-11',
            'id':1,
            'teamlead' : {'id':1,'name':'Глуховський'}
        },
        {
            'name': u'ПАПА',
            'id': 2,
            'teamlead': {'id': 2, 'name': 'Чорненький'}
        },
        {
            'name': u'ПМ22',
            'id': 3,
            'teamlead' : {'id':3,'name':'ДСША'}
        },
    )
    return render(request, 'students/groups_list.html',{'groups':groups})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)