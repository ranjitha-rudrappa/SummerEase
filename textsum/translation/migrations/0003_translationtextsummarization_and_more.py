# Generated by Django 4.1.13 on 2023-12-13 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0002_alter_textsummarization_generated_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='TranslationTextSummarization',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('input_text', models.TextField()),
                ('generated_summary', models.TextField()),
                ('translated_summary', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='TextSummarization',
        ),
    ]
