# Generated by Django 3.2.12 on 2022-04-10 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('georga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Einsatzort',
                'verbose_name_plural': 'Einsatzorte',
            },
        ),
        migrations.CreateModel(
            name='PollChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('max_participants', models.IntegerField(default=1)),
                ('persons', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Umfrageoption',
                'verbose_name_plural': 'Umfrageoptionen',
            },
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2000)),
                ('style', models.CharField(choices=[('default', 'default')], default='default', max_length=20)),
                ('choices', models.ManyToManyField(blank=True, to='georga.PollChoice')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='georga.location')),
            ],
            options={
                'verbose_name': 'Umfrage',
                'verbose_name_plural': 'Umfragen',
            },
        ),
    ]
