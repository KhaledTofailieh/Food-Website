# Generated by Django 3.1.3 on 2021-08-10 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_delete_marketingstrategy'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketingStrategy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('key', models.CharField(max_length=50)),
                ('description', models.CharField(default='', max_length=200, null=True)),
                ('url', models.CharField(default='', max_length=50, null=True)),
                ('isActive', models.BooleanField(default=False)),
            ],
        ),
    ]
