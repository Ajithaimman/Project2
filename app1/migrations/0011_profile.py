# Generated by Django 5.0.1 on 2024-04-09 09:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_register_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locality', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Goa', 'Goa'), ('Tamilnadu', 'Tamilnadu'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Orissa', 'Orissa')], max_length=100)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.register')),
            ],
        ),
    ]
