# Generated by Django 3.1.2 on 2020-10-29 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20201029_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertising',
            name='year',
            field=models.CharField(blank=True, choices=[('الأولى', 'الأولى'), ('الثانية', 'الثانية'), ('الثالثة', 'الثالثة'), ('الرابعة', 'الرابعة'), ('الخامسة', 'الخامسة')], max_length=20, null=True),
        ),
    ]