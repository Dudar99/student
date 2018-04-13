# -*- coding: utf-8 -*-

from django.db import models
from  .student import Student


class Journal(models.Model):

    class Meta(object):
        verbose_name = u'Відвідування'
        verbose_name_plural = u'Відвідування'


    student = models.ForeignKey(Student, verbose_name='Студент',blank=False,null=True)

    month = models.DateField(blank=False, verbose_name=u"Дата відвідування")
    ### Day of the certain month

    day1 = models.BooleanField(default=False)
    day2 = models.BooleanField(default=False)
    day3 = models.BooleanField(default=False)
    day4 = models.BooleanField(default=False)
    day5 = models.BooleanField(default=False)
    day6 = models.BooleanField(default=False)
    day7 = models.BooleanField(default=False)
    day8 = models.BooleanField(default=False)
    day9 = models.BooleanField(default=False)
    day10 = models.BooleanField(default=False)
    day11 = models.BooleanField(default=False)
    day12 = models.BooleanField(default=False)
    day13 = models.BooleanField(default=False)
    day14 = models.BooleanField(default=False)
    day15 = models.BooleanField(default=False)
    day16 = models.BooleanField(default=False)
    day17 = models.BooleanField(default=False)
    day18 = models.BooleanField(default=False)
    day19 = models.BooleanField(default=False)
    day20 = models.BooleanField(default=False)
    day21 = models.BooleanField(default=False)
    day22 = models.BooleanField(default=False)
    day23 = models.BooleanField(default=False)
    day24 = models.BooleanField(default=False)
    day25 = models.BooleanField(default=False)
    day26 = models.BooleanField(default=False)
    day27  = models.BooleanField(default=False)
    day28= models.BooleanField(default=False)
    day29= models.BooleanField(default=False)
    day30= models.BooleanField(default=False)
    day31= models.BooleanField(default=False)


    def __unicode__(self):
        return ("%s ( %d - %d)") % (self.student.last_name,self.month.year,self.month.month)