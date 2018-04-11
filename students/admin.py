# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Student
from .models import Group
from django.contrib import admin

admin.site.register(Student)
admin.site.register(Group)