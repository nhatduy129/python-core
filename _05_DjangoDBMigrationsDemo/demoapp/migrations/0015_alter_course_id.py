# Generated by Django 5.0.4 on 2025-02-20 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0014_alter_course_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
