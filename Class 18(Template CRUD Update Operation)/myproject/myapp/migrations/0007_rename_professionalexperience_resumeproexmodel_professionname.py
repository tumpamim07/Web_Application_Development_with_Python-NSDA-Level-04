# Generated by Django 5.0.7 on 2024-08-09 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_resumeproexmodel_professionalresponsibilities'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resumeproexmodel',
            old_name='ProfessionalExperience',
            new_name='ProfessionName',
        ),
    ]
