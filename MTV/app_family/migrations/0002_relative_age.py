# Generated by Django 4.0.4 on 2022-05-19 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_family', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='relative',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
