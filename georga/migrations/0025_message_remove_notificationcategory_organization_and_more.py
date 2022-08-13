# Generated by Django 4.1 on 2022-08-13 00:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('georga', '0024_remove_role_amount_participant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('object_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('title', models.CharField(max_length=100)),
                ('contents', models.CharField(max_length=1000)),
                ('priority', models.CharField(choices=[('DISTURB', 'disturb'), ('ONAPPCALL', 'on app call'), ('ONNEWS', 'on reading news actively')], default='ONNEWS', max_length=9)),
                ('category', models.CharField(choices=[('NEWS', 'news'), ('ALERT', 'alert'), ('ACTIVITY', 'activity')], default='NEWS', max_length=8)),
                ('state', models.CharField(choices=[('DRAFT', 'draft'), ('PUBLISHED', 'published')], default='DRAFT', max_length=9)),
                ('delivery_state', models.CharField(choices=[('NONE', 'none'), ('PENDING', 'pending'), ('SENT', 'sent'), ('SENT_SUCCESSFULLY', 'sent successfully'), ('SENT_ERROR', 'sent error')], default='NONE', max_length=17)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='notificationcategory',
            name='organization',
        ),
        migrations.AddField(
            model_name='persontoobject',
            name='bookmarked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='persontoobject',
            name='unseen',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
        migrations.DeleteModel(
            name='NotificationCategory',
        ),
    ]
