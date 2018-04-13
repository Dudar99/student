# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20180413_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name='\u041d\u0430\u0437\u0432\u0430')),
                ('date', models.DateTimeField(verbose_name='\u0427\u0430\u0441 \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u043d\u044f')),
                ('lector_name', models.CharField(max_length=250, verbose_name='\u0412\u0438\u043a\u043b\u0430\u0434\u0430\u0447', blank=True)),
                ('exam_group', models.ForeignKey(verbose_name='\u0413\u0440\u0443\u043f\u0430', to='students.Group')),
            ],
            options={
                'verbose_name': '\u0415\u043a\u0437\u0430\u043c\u0435\u043d',
                'verbose_name_plural': '\u0415\u043a\u0437\u0430\u043c\u0435\u043d\u0438',
            },
            bases=(models.Model,),
        ),
    ]
