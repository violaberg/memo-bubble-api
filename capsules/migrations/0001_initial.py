# Generated by Django 4.2.7 on 2024-06-25 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Capsule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('release_date', models.DateTimeField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='memo-bubble/videos/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('capsule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='capsules.capsule')),
            ],
            options={
                'verbose_name_plural': 'Videos',
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='memo-bubble/images/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('capsule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='capsules.capsule')),
            ],
            options={
                'verbose_name_plural': 'Images',
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='GeminiMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('capsule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gemini_messages', to='capsules.capsule')),
            ],
            options={
                'verbose_name_plural': 'Gemini Messages',
                'ordering': ['-created_on'],
            },
        ),
    ]
