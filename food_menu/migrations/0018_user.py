# Generated by Django 3.1.3 on 2021-08-30 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_menu', '0017_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
            ],
        ),
    ]
