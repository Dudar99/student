# -*- coding: utf-8 -*-


from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator


def contact(request):
    return render(request,"students/contact-admin.html",{})
from django import forms
class ContancForm(forms.Form):
    form_email = forms.EmailField(label=u'Емейл адреса')
    subject = forms.CharField(max_length=123,label=u'Заголовок листа')
    message = forms.CharField(max_length = 800,label=u"Текст повідомлення",widget=forms.Textarea)