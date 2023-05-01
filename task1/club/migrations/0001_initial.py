# Generated by Django 4.1.3 on 2023-05-01 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('com_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('com_winner', models.CharField(default='no winners', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Footballclub',
            fields=[
                ('fc_id', models.IntegerField(primary_key=True, serialize=False)),
                ('club_logo', models.CharField(max_length=240)),
                ('fc_name', models.CharField(max_length=255)),
                ('description', models.TextField(default='')),
                ('fc_email', models.EmailField(max_length=254)),
                ('fc_stadium', models.TextField(default='')),
                ('fc_location', models.TextField(default='')),
                ('position', models.IntegerField()),
                ('competing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compi', to='club.competition')),
                ('managers', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='users.manager')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('match_timing', models.TextField(default='')),
                ('match_location', models.TextField(primary_key=True, serialize=False)),
                ('playedby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.footballclub')),
                ('refereed_by', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='users.referee')),
            ],
        ),
    ]
