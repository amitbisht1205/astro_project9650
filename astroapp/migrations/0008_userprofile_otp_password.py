# Generated by Django 4.2.7 on 2023-12-05 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astroapp', '0007_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='otp_password',
            field=models.CharField(default='phone', max_length=6),
            preserve_default=False,
        ),
    ]
