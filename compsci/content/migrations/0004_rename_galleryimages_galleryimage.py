# Generated by Django 3.2.6 on 2021-08-10 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_alter_userprofile_teacher'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GalleryImages',
            new_name='GalleryImage',
        ),
    ]
