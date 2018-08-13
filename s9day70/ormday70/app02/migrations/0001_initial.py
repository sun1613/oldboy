# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-09 16:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Author2Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app02.Author')),
            ],
        ),
        migrations.CreateModel(
            name='AuthorDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bobby', models.CharField(max_length=32)),
                ('addr', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('publish_date', models.DateField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app02.Publisher'),
        ),
        migrations.AddField(
            model_name='author2book',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app02.Book'),
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='app02.Book'),
        ),
        migrations.AddField(
            model_name='author',
            name='detail',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app02.AuthorDetail'),
        ),
        migrations.AlterUniqueTogether(
            name='author2book',
            unique_together=set([('author', 'book')]),
        ),
    ]
