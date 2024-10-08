# Generated by Django 5.0.4 on 2024-04-23 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_custom_user_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JobTitle', models.CharField(max_length=50, null=True)),
                ('CompanyName', models.CharField(max_length=50, null=True)),
                ('Address', models.CharField(max_length=50, null=True)),
                ('CompanyDescription', models.TextField(null=True)),
                ('JobDescription', models.TextField(null=True)),
                ('Qualification', models.CharField(max_length=50, null=True)),
                ('SalaryInformation', models.CharField(max_length=50, null=True)),
                ('Deadline', models.DateField(null=True)),
                ('Designation', models.CharField(max_length=50, null=True)),
                ('Experience', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='custom_user',
            name='user_type',
            field=models.CharField(choices=[('job_seeker', 'Job_Seeker'), ('job_recruiter', 'Job_Recruiter')], max_length=50, null=True),
        ),
    ]
