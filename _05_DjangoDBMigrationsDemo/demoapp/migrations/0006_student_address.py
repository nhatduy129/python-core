# Generated by Django 5.1.6 on 2025-02-18 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0005_alter_student_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.TextField(default='123'),
        ),
    ]
