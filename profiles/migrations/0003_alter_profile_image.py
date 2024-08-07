# Generated by Django 4.2.7 on 2024-07-29 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='https://memo-bubble-app.s3.eu-west-1.amazonaws.com/media/memo-bubble/placeholder/placeholder.png', upload_to='memo-bubble/profile_images'),
        ),
    ]
