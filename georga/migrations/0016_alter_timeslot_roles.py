# Generated by Django 3.2.14 on 2022-08-07 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('georga', '0015_role_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='roles',
            field=models.ManyToManyField(related_name='timeslot_roles', to='georga.Role'),
        ),
    ]
