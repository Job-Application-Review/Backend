# Generated by Django 3.2.13 on 2022-05-24 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_application_completed'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.RemoveField(
            model_name='application',
            name='title',
        ),
    ]
