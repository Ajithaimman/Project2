# Generated by Django 5.0.1 on 2024-04-10 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_delete_profile_delete_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=30)),
                ('cpassword', models.CharField(max_length=30)),
            ],
        ),
    ]
