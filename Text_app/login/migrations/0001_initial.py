# Generated by Django 4.1.13 on 2023-12-14 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(default='default_username', max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('reset_password_token', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
    ]
