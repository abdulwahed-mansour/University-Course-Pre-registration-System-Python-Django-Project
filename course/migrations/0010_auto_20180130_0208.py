# Generated by Django 2.0 on 2018-01-29 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_takencourse_gpa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courselist',
            name='course_code',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]