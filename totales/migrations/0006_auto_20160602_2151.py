# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20160525_1958'),
        ('totales', '0005_auto_20160602_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle_Compra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
                ('precio', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
                ('product', models.ForeignKey(to='product.Product', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='product',
        ),
        migrations.AlterField(
            model_name='compras',
            name='product',
            field=models.ManyToManyField(to='product.Product', through='totales.Detalle_Compra'),
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.AddField(
            model_name='detalle_compra',
            name='provider',
            field=models.ForeignKey(to='totales.Compras'),
        ),
    ]
