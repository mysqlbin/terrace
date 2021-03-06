# Generated by Django 2.0.5 on 2019-10-22 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20190923_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='db_account',
            name='account',
        ),
        migrations.RemoveField(
            model_name='db_account',
            name='dbname',
        ),
        migrations.RemoveField(
            model_name='db_name',
            name='account',
        ),
        migrations.AddField(
            model_name='db_instance',
            name='password',
            field=models.CharField(blank=True, default='', max_length=300, verbose_name='密码'),
        ),
        migrations.AddField(
            model_name='db_instance',
            name='user',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='用户名'),
        ),
        migrations.RemoveField(
            model_name='db_name',
            name='instance',
        ),
        migrations.AddField(
            model_name='db_name',
            name='instance',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.Db_instance'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Db_account',
        ),
    ]
