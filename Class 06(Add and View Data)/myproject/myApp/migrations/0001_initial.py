# Generated by Django 5.0.3 on 2024-03-22 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('stdid', models.CharField(max_length=50)),
                ('dept', models.CharField(max_length=50)),
            ],
        ),
    ]
