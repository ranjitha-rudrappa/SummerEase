# Generated by Django 4.1.13 on 2024-02-06 04:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_to_summary', '0006_pdfdocument_user1'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfdocument',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
