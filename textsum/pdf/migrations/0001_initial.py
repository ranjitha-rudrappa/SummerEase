# Generated by Django 4.1.13 on 2023-11-28 09:25

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PdfDocument',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('pdf_file', models.FileField(upload_to='pdfs/')),
                ('summarized_text', models.TextField()),
                ('pages_to_summarize', models.CharField(max_length=255)),
            ],
        ),
    ]
