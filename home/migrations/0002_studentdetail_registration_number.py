# Generated by Django 4.0.3 on 2022-03-28 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetail',
            name='registration_number',
            field=models.IntegerField(default=30),
        ),
    ]
