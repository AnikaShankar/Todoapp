# Generated by Django 2.1.2 on 2018-11-26 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_auto_20181126_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='title',
        ),
        migrations.AlterField(
            model_name='todo',
            name='Todo',
            field=models.CharField(max_length=600),
        ),
    ]
