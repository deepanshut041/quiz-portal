# Generated by Django 2.0.6 on 2018-06-09 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selectedanswer',
            name='coreect_or_not',
        ),
    ]
