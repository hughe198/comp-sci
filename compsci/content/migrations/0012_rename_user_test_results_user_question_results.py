# Generated by Django 3.2.2 on 2021-07-21 20:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0011_auto_20210721_2103'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_Test_Results',
            new_name='User_Question_Results',
        ),
    ]