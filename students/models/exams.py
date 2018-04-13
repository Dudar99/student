# -*- coding: utf-8 -*-

from django.db import models
from  .group import Group

class Exam(models.Model):

    class Meta(object):
        verbose_name = u"Екзамен"
        verbose_name_plural = u"Екзамени"
    name = models.CharField(max_length=250,blank=False,verbose_name=u"Назва")
    date = models.DateTimeField(blank=False,verbose_name=u"Час проведення")

    lector_name = models.CharField(max_length=250,blank=True,verbose_name=u'Викладач')
    exam_group = models.ForeignKey(Group,blank=False,verbose_name=u"Група")
    def __unicode__(self):
        return u"%s (%s)" % (self.name,self.exam_group.title)