# Generated by Django 3.2.14 on 2022-08-06 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('georga', '0011_auto_20220806_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='notificationcategory',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
