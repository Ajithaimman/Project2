# Generated by Django 5.0.1 on 2024-03-16 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='composition',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='prodapp',
        ),
    ]
