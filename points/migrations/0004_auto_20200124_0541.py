# Generated by Django 3.0.2 on 2020-01-24 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0003_auto_20200124_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
