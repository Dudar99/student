# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import PageNotAnInteger,EmptyPage,Paginator

from ..models.exams import Exam

def exams_list(request):
    exams = Exam.objects.all()
    return render(request, 'students/exams.html',{'exams':exams})
