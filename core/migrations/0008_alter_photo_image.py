# Generated by Django 5.1.1 on 2024-10-29 10:08

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_project_slug_alter_project_conclusion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='portfolio/project-images/'),
        ),
    ]