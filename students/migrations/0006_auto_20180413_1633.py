# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20180413_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='month',
            field=models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0432\u0456\u0434\u0432\u0456\u0434\u0443\u0432\u0430\u043d\u043d\u044f'),
            preserve_default=True,
        ),
    ]
