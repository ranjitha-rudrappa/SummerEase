# Generated by Django 4.1.13 on 2024-01-23 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_to_summary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfdocument',
            name='user1',
            field=models.IntegerField(default=0),
        ),
    ]
