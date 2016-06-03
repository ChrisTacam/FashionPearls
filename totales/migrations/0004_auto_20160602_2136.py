# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0001_initial'),
        ('totales', '0003_auto_20160602_2124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('invoice', models.CharField(max_length=10, null=True, verbose_name=b'invoice')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name=b'date')),
                ('provider', models.ForeignKey(to='provider.Provider', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='author',
            name='provider',
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(to='totales.Compras'),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
