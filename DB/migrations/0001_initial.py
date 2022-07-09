# Generated by Django 3.1.7 on 2021-06-02 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataAboutUserAndVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_user', models.IntegerField(default=False)),
                ('ID_video_information', models.IntegerField(default=False)),
                ('ID_screenshot', models.IntegerField(default=False)),
                ('dominant_emotion', models.CharField(max_length=50)),
                ('edited_dominant_emotion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DominantEmotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dominant_emotion', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=15)),
                ('age', models.IntegerField(default=False)),
                ('male', models.BooleanField(default=False)),
                ('female', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='VideoInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=800)),
            ],
        ),
    ]