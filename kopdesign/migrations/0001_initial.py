# Generated by Django 3.0.2 on 2020-02-10 16:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('linkToImg', models.URLField()),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('url', models.URLField(default=None)),
            ],
        ),
    ]