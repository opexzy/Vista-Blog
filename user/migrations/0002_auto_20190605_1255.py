# Generated by Django 2.2.2 on 2019-06-05 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginmodel',
            name='first_name',
            field=models.CharField(default='unset', max_length=50),
        ),
        migrations.AlterField(
            model_name='loginmodel',
            name='last_login',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='loginmodel',
            name='last_name',
            field=models.CharField(default='unset', max_length=50),
        ),
        migrations.AlterField(
            model_name='loginmodel',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='loginmodel',
            name='status',
            field=models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=0),
        ),
        migrations.AlterField(
            model_name='loginmodel',
            name='user_type',
            field=models.IntegerField(choices=[(1, 'Administrator'), (2, 'Moderator'), (3, 'Author')], default=3),
        ),
    ]
