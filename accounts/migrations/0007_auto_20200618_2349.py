# Generated by Django 3.0.7 on 2020-06-18 20:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200618_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(2)], verbose_name='جوال'),
        ),
    ]
