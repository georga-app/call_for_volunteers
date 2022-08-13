# Generated by Django 3.2.14 on 2022-08-07 14:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('georga', '0012_auto_20220806_0029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(default='', max_length=30)),
                ('owner', models.CharField(choices=[('SELF', 'person itself'), ('ORG', 'provided by organization'), ('THIRDPARTY', 'other party')], default='ORG', max_length=10)),
            ],
            options={
                'verbose_name': 'equipment',
                'verbose_name_plural': 'equipment',
            },
        ),
        migrations.DeleteModel(
            name='EquipmentProvided',
        ),
        migrations.DeleteModel(
            name='EquipmentSelf',
        ),
        migrations.AddField(
            model_name='deployment',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='role',
            name='is_template',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='role',
            name='qualifications_suitable',
            field=models.ManyToManyField(blank=True, related_name='qualifications_suitable', to='georga.Qualification'),
        ),
        migrations.AddField(
            model_name='resource',
            name='equipment_needed',
            field=models.ManyToManyField(blank=True, related_name='equipment_needed', to='georga.Equipment'),
        ),
    ]