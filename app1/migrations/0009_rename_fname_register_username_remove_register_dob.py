# Generated by Django 5.0.1 on 2024-03-21 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_register'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='fname',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='register',
            name='dob',
        ),
    ]
