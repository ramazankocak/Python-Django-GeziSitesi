# Generated by Django 3.2.2 on 2021-05-22 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yurtdışı', '0002_rename_yurtiçi_yurtdışı'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yurtdışı',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Yurtdışı',
        ),
    ]
