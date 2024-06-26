# Generated by Django 4.2.7 on 2024-06-26 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capsules', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geminimessage',
            name='capsule',
        ),
        migrations.AddField(
            model_name='geminimessage',
            name='images',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='gemini_messages', to='capsules.image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='geminimessage',
            name='videos',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='gemini_messages', to='capsules.video'),
            preserve_default=False,
        ),
    ]