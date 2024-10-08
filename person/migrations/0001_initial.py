# Generated by Django 4.2.15 on 2024-08-16 17:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63, null=True)),
                ('last_name', models.CharField(max_length=63, null=True)),
                ('national_id', models.CharField(default='0000000000', max_length=10, validators=[django.core.validators.RegexValidator('\\d{10}$', 'invalid')])),
            ],
        ),
    ]
