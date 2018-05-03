# -*- coding: utf-8 -*-


from __future__ import unicode_literals
from django.shortcuts import render
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from studentsdb.settings import ADMIN_EMAIL
from django import forms

class ContancForm(forms.Form):
    from_email = forms.EmailField(label=u'Емейл адреса')
    subject = forms.CharField(max_length=123,label=u'Заголовок листа')
    message = forms.CharField(max_length =800,label=u"Текст повідомлення",widget=forms.Textarea)



def contact(request):
    # if button submit was pressed
    if request.method == "POST":
        form = ContancForm(request.POST)
        # CHECK IF FORM IS VALID
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']
            try:
                send_mail(subject,message,from_email,[ADMIN_EMAIL])
            except Exception:
                message = u"Під час відправки листа сталася помилка"
            else:
                message = u'Повідомлення успішно надіслано'
                #redirect to form page with success message
                return HttpResponseRedirect(u'%s?status_mesage=%s'%(reverse('contact_admin'),message))
    else:
        form = ContancForm()

    return render(request,"students/contact-admin.html",{'form':form})
