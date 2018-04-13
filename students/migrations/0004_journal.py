# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_student_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('month', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u043d\u044f')),
                ('day1', models.BooleanField(default=False)),
                ('day2', models.BooleanField(default=False)),
                ('day3', models.BooleanField(default=False)),
                ('day4', models.BooleanField(default=False)),
                ('day5', models.BooleanField(default=False)),
                ('day6', models.BooleanField(default=False)),
                ('day7', models.BooleanField(default=False)),
                ('day8', models.BooleanField(default=False)),
                ('day9', models.BooleanField(default=False)),
                ('day10', models.BooleanField(default=False)),
                ('day11', models.BooleanField(default=False)),
                ('day12', models.BooleanField(default=False)),
                ('day13', models.BooleanField(default=False)),
                ('day14', models.BooleanField(default=False)),
                ('day15', models.BooleanField(default=False)),
                ('day16', models.BooleanField(default=False)),
                ('day17', models.BooleanField(default=False)),
                ('day18', models.BooleanField(default=False)),
                ('day19', models.BooleanField(default=False)),
                ('day20', models.BooleanField(default=False)),
                ('day21', models.BooleanField(default=False)),
                ('day22', models.BooleanField(default=False)),
                ('day23', models.BooleanField(default=False)),
                ('day24', models.BooleanField(default=False)),
                ('day25', models.BooleanField(default=False)),
                ('day26', models.BooleanField(default=False)),
                ('day27', models.BooleanField(default=False)),
                ('day28', models.BooleanField(default=False)),
                ('day29', models.BooleanField(default=False)),
                ('day30', models.BooleanField(default=False)),
                ('day31', models.BooleanField(default=False)),
                ('student', models.ForeignKey(verbose_name=b'\xd0\xa1\xd1\x82\xd1\x83\xd0\xb4\xd0\xb5\xd0\xbd\xd1\x82', to='students.Student', null=True)),
            ],
            options={
                'verbose_name': '\u0412\u0456\u0434\u0432\u0456\u0434\u0443\u0432\u0430\u043d\u043d\u044f',
            },
            bases=(models.Model,),
        ),
    ]
