# Generated by Django 5.1.1 on 2024-09-24 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_project_description_remove_project_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='portfolio/project-images/'),
        ),
    ]
