# Generated by Django 5.0.2 on 2024-02-24 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_product_composition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('ty1', 'toys1'), ('ty2', 'toys2'), ('ty3', 'toys3'), ('ty4', 'toys4'), ('ty5', 'toys5'), ('ty6', 'toys6')], max_length=100),
        ),
    ]
