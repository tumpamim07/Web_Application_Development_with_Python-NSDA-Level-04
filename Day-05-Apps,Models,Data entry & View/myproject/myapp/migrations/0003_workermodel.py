# Generated by Django 5.0.3 on 2024-03-19 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_teachermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='workerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name2', models.CharField(max_length=20)),
                ('workid', models.CharField(max_length=20)),
            ],
        ),
    ]
