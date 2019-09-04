# Generated by Django 2.0.5 on 2019-06-27 16:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190627_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='db_instance',
            name='charset',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='db_instance',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2019, 6, 27, 16, 13, 3, 268681)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='db_instance',
            name='instance_name',
            field=models.CharField(default=datetime.datetime(2019, 6, 27, 16, 13, 7, 190681), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='db_instance',
            name='type',
            field=models.CharField(choices=[('master', '主库'), ('slave', '从库')], default='', max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='db_instance',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='db_instance',
            name='db_type',
            field=models.CharField(choices=[('mysql', 'MySQL'), ('mongodb', 'MongoDB'), ('mssql', 'MsSQL'), ('redis', 'Redis'), ('pgsql', 'PgSQL'), ('oracle', 'Oracle')], default='mysql', max_length=30),
        ),
    ]