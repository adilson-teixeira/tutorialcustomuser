# Generated by Django 4.0 on 2021-12-30 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cliente',
            field=models.TextField(blank=True),
        ),
    ]
