# Generated by Django 5.0.4 on 2025-02-20 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0017_alter_course_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='score',
            field=models.IntegerField(),
        ),
    ]
