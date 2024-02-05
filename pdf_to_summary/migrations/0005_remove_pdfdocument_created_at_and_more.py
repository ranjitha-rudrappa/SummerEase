# Generated by Django 4.1.13 on 2024-02-05 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_to_summary', '0004_remove_pdfdocument_summarized_text_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pdfdocument',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='pdfdocument',
            name='summarized_text1',
        ),
        migrations.RemoveField(
            model_name='pdfdocument',
            name='user1',
        ),
        migrations.AddField(
            model_name='pdfdocument',
            name='summarized_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]