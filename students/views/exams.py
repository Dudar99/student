# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import PageNotAnInteger,EmptyPage,Paginator

from ..models.exams import Exam

def exams_list(request):
    exams = Exam.objects.all()
    order_by = request.GET.get('order_by','')
    if order_by in ('name','date'):
        exams = exams.order_by(order_by)
        if request.GET.get('reverse',''):
            exams = exams.reverse()
    if request.get_full_path() == "/exams/":  ### код який автоматично загружає сторінку з фільтром
        # redirect request.GET on its copy(deep copy) which I will amend    ### але не міняє самої урли
        request.GET = request.GET.copy()
        # assign 'order_by' value 'name'
        request.GET.__setitem__('order_by', 'date')
    return render(request, 'students/exams.html',{'exams':exams})
