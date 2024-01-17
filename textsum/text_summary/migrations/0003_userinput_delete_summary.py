# Generated by Django 4.1.13 on 2023-12-13 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text_summary', '0002_rename_textgeneration_summary_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('summary', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Summary',
        ),
    ]