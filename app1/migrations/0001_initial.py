# Generated by Django 5.0.2 on 2024-02-17 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TimeField()),
                ('composition', models.TimeField()),
                ('prodapp', models.TextField()),
                ('category', models.CharField(choices=[('ty', 'toys1'), ('ty', 'toys2'), ('ty', 'toys3'), ('ty', 'toys4'), ('ty', 'toys5'), ('ty', 'toys6')], max_length=100)),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
    ]