# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator

from ..models.group import Group


# Views for Groups
def groups_list(request):
    groups = Group.objects.all()
    if request.get_full_path() == "/groups/":  ### код який автоматично загружає сторінку з фільтром
        # redirect request.GET on its copy(deep copy) which I will amend    ### але не міняє самої урли
        request.GET = request.GET.copy()
        # assign 'order_by' value 'last_name'
        request.GET.__setitem__('order_by', 'title')
    order_by = request.GET.get('order_by', '')
    if order_by in ('title',):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', ''):
            groups = groups.reverse()
    paginator = Paginator(groups, 2)
    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        groups = paginator.page(1)
    except EmptyPage:
        groups = paginator.page(paginator.num_pages)
    return render(request, 'students/groups_list.html', {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
