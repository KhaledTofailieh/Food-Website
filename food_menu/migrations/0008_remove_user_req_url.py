# Generated by Django 3.1.3 on 2021-08-10 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_menu', '0007_user_req_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='req_url',
        ),
    ]
