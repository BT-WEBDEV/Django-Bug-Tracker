# Generated by Django 3.0.6 on 2020-08-18 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0008_auto_20200803_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='priority',
            name='priority',
        ),
        migrations.AddField(
            model_name='priority',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
