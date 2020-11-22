# Generated by Django 3.0.2 on 2020-09-19 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('video_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('url', models.CharField(max_length=200, unique=True)),
                ('cover_url', models.CharField(max_length=200, unique=True)),
                ('svi_raw', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('visitor_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=100, unique=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('pid', models.CharField(max_length=100, unique=True)),
                ('video', models.ForeignKey(db_column='video', null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Video')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('session_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('pid', models.CharField(max_length=100)),
                ('visitor', models.ForeignKey(db_column='visitor', null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Visitor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField()),
                ('video_time', models.DecimalField(decimal_places=6, max_digits=12)),
                ('volume', models.DecimalField(decimal_places=2, max_digits=3)),
                ('buffered', models.IntegerField()),
                ('playback_rate', models.DecimalField(decimal_places=2, max_digits=3)),
                ('full_page', models.BooleanField()),
                ('full_screen', models.BooleanField()),
                ('player_height', models.IntegerField()),
                ('player_width', models.IntegerField()),
                ('session', models.ForeignKey(db_column='session', null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Session')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]