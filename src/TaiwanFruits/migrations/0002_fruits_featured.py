# Generated by Django 2.0.7 on 2020-08-27 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaiwanFruits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruits',
            name='featured',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
