# Generated by Django 3.2.6 on 2021-08-19 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_auto_20210819_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_set',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='content.questionset'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.topic'),
        ),
    ]
