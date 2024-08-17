# Generated by Django 5.0.4 on 2024-04-22 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='custom_user',
            name='DOB',
            field=models.DateField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='custom_user',
            name='FirstName',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='custom_user',
            name='Image',
            field=models.ImageField(null=True, upload_to='Project_image/image'),
        ),
        migrations.AddField(
            model_name='custom_user',
            name='LastName',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='custom_user',
            name='blood',
            field=models.CharField(choices=[('recruiter', 'Recruiter'), ('jobseeker', 'JobSeeker')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='custom_user',
            name='gender',
            field=models.CharField(choices=[('recruiter', 'Recruiter'), ('jobseeker', 'JobSeeker')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='custom_user',
            name='display_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='custom_user',
            name='user_type',
            field=models.CharField(choices=[('recruiter', 'Recruiter'), ('jobseeker', 'JobSeeker')], max_length=50, null=True),
        ),
    ]
