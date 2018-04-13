# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from ..models.journal import Journal
def journal_list(request):
    students =Journal.objects.all()
    return render(request, 'students/journal.html', {'students': students})
