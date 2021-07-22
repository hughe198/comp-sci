# Generated by Django 3.2.2 on 2021-07-21 21:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0012_rename_user_test_results_user_question_results'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/question/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/question/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User_Question_Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.question')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='absquestion',
            name='topic_id',
        ),
        migrations.RemoveField(
            model_name='checkboxanswer',
            name='absanswer_ptr',
        ),
        migrations.RemoveField(
            model_name='checkboxquestion',
            name='absquestion_ptr',
        ),
        migrations.RemoveField(
            model_name='radiobtnanswer',
            name='absanswer_ptr',
        ),
        migrations.RemoveField(
            model_name='radiobtnquestion',
            name='absquestion_ptr',
        ),
        migrations.RemoveField(
            model_name='user_question_results',
            name='question_id',
        ),
        migrations.RemoveField(
            model_name='user_question_results',
            name='topic_id',
        ),
        migrations.RemoveField(
            model_name='user_question_results',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tags',
            name='question_id',
        ),
        migrations.RemoveField(
            model_name='topics',
            name='num_questions',
        ),
        migrations.AlterField(
            model_name='tags',
            name='tag',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='ABSAnswer',
        ),
        migrations.DeleteModel(
            name='ABSQuestion',
        ),
        migrations.DeleteModel(
            name='CheckBoxAnswer',
        ),
        migrations.DeleteModel(
            name='CheckBoxQuestion',
        ),
        migrations.DeleteModel(
            name='RadioBTNAnswer',
        ),
        migrations.DeleteModel(
            name='RadioBtnQuestion',
        ),
        migrations.DeleteModel(
            name='User_Question_Results',
        ),
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.topics'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.question'),
        ),
        migrations.AddField(
            model_name='tags',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.question'),
        ),
    ]
