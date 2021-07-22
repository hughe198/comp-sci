# Generated by Django 3.2.2 on 2021-07-21 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0010_alter_galleryimages_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ABSAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ABSQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.TextField()),
                ('num_questions', models.SmallIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CheckBoxAnswer',
            fields=[
                ('absanswer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.absanswer')),
                ('answer', models.TextField()),
                ('correct', models.BooleanField(default=False)),
            ],
            bases=('content.absanswer',),
        ),
        migrations.CreateModel(
            name='CheckBoxQuestion',
            fields=[
                ('absquestion_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.absquestion')),
                ('question', models.TextField()),
            ],
            bases=('content.absquestion',),
        ),
        migrations.CreateModel(
            name='RadioBTNAnswer',
            fields=[
                ('absanswer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.absanswer')),
                ('answer', models.TextField()),
                ('correct', models.BooleanField(default=False)),
            ],
            bases=('content.absanswer',),
        ),
        migrations.CreateModel(
            name='RadioBtnQuestion',
            fields=[
                ('absquestion_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.absquestion')),
                ('question', models.TextField()),
            ],
            bases=('content.absquestion',),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/content/profiles')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_Test_Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct', models.BooleanField(default=False)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.absquestion')),
                ('topic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.topics')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.TextField()),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.absquestion')),
            ],
        ),
        migrations.AddField(
            model_name='absquestion',
            name='topic_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.topics'),
        ),
        migrations.AddField(
            model_name='absanswer',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.absquestion'),
        ),
    ]
