# Generated by Django 2.2.4 on 2019-08-08 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_profile_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]