# Generated by Django 4.1 on 2022-08-07 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_studentprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='mobile_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='registration_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='yearsofstudy',
            field=models.IntegerField(),
        ),
    ]
