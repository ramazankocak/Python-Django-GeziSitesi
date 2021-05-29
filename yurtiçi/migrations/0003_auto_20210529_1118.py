# Generated by Django 3.2.2 on 2021-05-29 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yurtiçi', '0002_auto_20210522_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bölge',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='şehirler',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('şehirler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yurtiçi.şehirler')),
            ],
        ),
    ]
