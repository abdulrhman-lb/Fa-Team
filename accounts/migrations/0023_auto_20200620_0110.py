# Generated by Django 3.0.7 on 2020-06-19 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_auto_20200620_0107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='branch',
            new_name='branchs',
        ),
    ]
