# Generated by Django 3.1.2 on 2020-10-19 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_subject_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='session',
            field=models.CharField(choices=[(1, 'فصل أول'), (1, 'فصل ثاني')], max_length=15),
        ),
    ]