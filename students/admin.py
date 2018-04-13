# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from students.models.student import Student
from students.models.group import Group
from students.models.journal import Journal
from students.models.exams import Exam
from django.contrib import admin

admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Journal)
admin.site.register(Exam)
# 0676887213