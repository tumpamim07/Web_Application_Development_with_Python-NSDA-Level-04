# Generated by Django 5.0.7 on 2024-08-09 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_socialmediamodel_instagram_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumeproexmodel',
            name='ProfessionalResponsibilities',
            field=models.TextField(null=True),
        ),
    ]
