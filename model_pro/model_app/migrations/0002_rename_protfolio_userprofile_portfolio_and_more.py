# Generated by Django 5.0.6 on 2024-05-30 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='protfolio',
            new_name='portfolio',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_pic'),
        ),
    ]
