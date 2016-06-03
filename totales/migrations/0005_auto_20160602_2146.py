# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20160525_1958'),
        ('totales', '0004_auto_20160602_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='product',
            field=models.ForeignKey(to='product.Product', null=True),
        ),
        migrations.AddField(
            model_name='compras',
            name='product',
            field=models.ManyToManyField(to='product.Product', through='totales.Book'),
        ),
    ]
