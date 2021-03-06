# Generated by Django 4.0.5 on 2022-06-14 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SystemAppModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.IntegerField()),
                ('title', models.CharField(max_length=20, verbose_name='科目名')),
                ('difficulty', models.FloatField(verbose_name='単位取得難易度')),
                ('amount_of_tasks', models.FloatField(verbose_name='課題の量')),
                ('credit', models.IntegerField(verbose_name='単位数')),
                ('term', models.CharField(max_length=10, verbose_name='学期')),
                ('teacher', models.CharField(max_length=50, verbose_name='担当教員')),
                ('way', models.CharField(max_length=50, verbose_name='授業方法')),
                ('evaluation', models.TextField(verbose_name='評価方法')),
                ('about', models.TextField(verbose_name='概要')),
            ],
        ),
    ]
