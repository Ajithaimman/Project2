# Generated by Django 5.0.1 on 2024-03-21 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_remove_product_composition_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('password', models.CharField(max_length=30)),
                ('cpassword', models.CharField(max_length=30)),
            ],
        ),
    ]