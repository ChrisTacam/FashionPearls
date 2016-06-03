# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totales', '0006_auto_20160602_2151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('cantidad', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
                ('precio', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='detalle_compra',
            name='product',
        ),
        migrations.RemoveField(
            model_name='detalle_compra',
            name='provider',
        ),
        migrations.RemoveField(
            model_name='compras',
            name='product',
        ),
        migrations.DeleteModel(
            name='Detalle_Compra',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(to='totales.Compras'),
        ),
    ]
