# Generated by Django 5.0.3 on 2024-04-01 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_studentmodel_studentimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachermodel',
            name='TImage',
            field=models.ImageField(null=True, upload_to='media/Teacher_Image'),
        ),
    ]
