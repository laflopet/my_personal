# Generated by Django 4.1.7 on 2023-04-06 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_remove_personas_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personas',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
