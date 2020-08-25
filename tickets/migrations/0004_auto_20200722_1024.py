# Generated by Django 3.0.6 on 2020-07-22 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20200721_1509'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BugDetails',
        ),
        migrations.RemoveField(
            model_name='bugenvironment',
            name='categories',
        ),
        migrations.DeleteModel(
            name='BugID',
        ),
        migrations.DeleteModel(
            name='BugOverview',
        ),
        migrations.AddField(
            model_name='ticket',
            name='actual_result',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='assigned_to',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='browser',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='categories',
            field=models.ManyToManyField(related_name='posts', to='tickets.Category'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='expected_result',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='image',
            field=models.FilePathField(blank=True, null=True, path='/img'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='operating_system',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='platform',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='priorities',
            field=models.ManyToManyField(related_name='posts', to='tickets.Priority'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='reporter',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='steps_to_reproduce',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='BugEnvironment',
        ),
    ]
