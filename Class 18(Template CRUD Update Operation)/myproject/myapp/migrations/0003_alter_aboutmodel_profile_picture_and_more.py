# Generated by Django 5.0.7 on 2024-08-09 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_aboutmodel_profile_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutmodel',
            name='Profile_Picture',
            field=models.ImageField(null=True, upload_to='media/ProfilePic'),
        ),
        migrations.AlterField(
            model_name='clienttestimonialmodel',
            name='ClientPic',
            field=models.ImageField(null=True, upload_to='media/ClientPic'),
        ),
    ]
