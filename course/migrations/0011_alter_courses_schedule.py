# Generated by Django 4.2.4 on 2023-09-18 16:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0010_remove_reply_email_alter_courses_schedule"),
    ]

    operations = [
        migrations.AlterField(
            model_name="courses",
            name="schedule",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 18, 9, 42, 35, 465532)
            ),
        ),
    ]
