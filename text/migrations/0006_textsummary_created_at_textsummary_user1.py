# Generated by Django 4.1.13 on 2024-01-25 06:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0005_textsummary_delete_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='textsummary',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='textsummary',
            name='user1',
            field=models.IntegerField(default=0),
        ),
    ]
