# Generated by Django 3.1.3 on 2021-07-27 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_menu', '0002_auto_20210727_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='img_url',
            field=models.ImageField(null=True, upload_to='pic'),
        ),
    ]
