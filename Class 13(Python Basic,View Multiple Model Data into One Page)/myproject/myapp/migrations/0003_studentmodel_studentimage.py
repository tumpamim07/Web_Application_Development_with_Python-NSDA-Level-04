# Generated by Django 5.0.3 on 2024-04-01 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_doctormodel_teachermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodel',
            name='StudentImage',
            field=models.ImageField(null=True, upload_to='media/Student_Image'),
        ),
    ]
