# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cantidad',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2),
        ),
        migrations.AddField(
            model_name='book',
            name='precio',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2),
        ),
    ]
