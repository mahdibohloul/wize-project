# Generated by Django 3.0 on 2019-12-17 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20191217_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='dead_line',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
