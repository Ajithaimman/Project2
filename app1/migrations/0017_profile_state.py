# Generated by Django 5.0.1 on 2024-04-11 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
