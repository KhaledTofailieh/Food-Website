# Generated by Django 3.1.3 on 2021-08-11 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_menu', '0010_delete_rest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('name_a', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('rest_id', models.CharField(max_length=10)),
            ],
        ),
    ]
