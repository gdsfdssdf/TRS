# Generated by Django 2.0 on 2018-01-25 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Photo', '0014_auto_20180125_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='province',
            name='pingyingName',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
