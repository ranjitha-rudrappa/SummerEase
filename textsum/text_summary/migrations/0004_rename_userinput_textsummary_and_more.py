# Generated by Django 4.1.13 on 2023-12-13 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('text_summary', '0003_userinput_delete_summary'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserInput',
            new_name='TextSummary',
        ),
        migrations.RenameField(
            model_name='textsummary',
            old_name='text',
            new_name='input_text',
        ),
    ]