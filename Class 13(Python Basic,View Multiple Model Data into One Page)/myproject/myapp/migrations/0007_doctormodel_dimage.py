# Generated by Django 5.0.3 on 2024-04-01 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_doctormodel_dimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctormodel',
            name='DImage',
            field=models.ImageField(null=True, upload_to='media/Doctor_Image'),
        ),
    ]
