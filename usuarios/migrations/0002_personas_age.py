# Generated by Django 4.1.7 on 2023-04-06 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personas',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
