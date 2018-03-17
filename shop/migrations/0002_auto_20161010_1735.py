# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-10 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='pic_back',
            field=models.ImageField(null=True, upload_to=b'itemspic'),
        ),
        migrations.AddField(
            model_name='item',
            name='pic_front',
            field=models.ImageField(null=True, upload_to=b'itemspic'),
        ),
        migrations.AddField(
            model_name='item',
            name='colour',
            field=models.ManyToManyField(to='shop.Colours'),
        ),
    ]
