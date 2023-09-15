# Generated by Django 4.2.4 on 2023-09-15 12:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0002_alter_courses_schedule_alter_courses_teacher"),
    ]

    operations = [
        migrations.AlterField(
            model_name="courses",
            name="image",
            field=models.ImageField(default="default.jpg", upload_to="courses"),
        ),
        migrations.AlterField(
            model_name="courses",
            name="schedule",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 15, 5, 51, 41, 618216)
            ),
        ),
        migrations.RemoveField(model_name="trainer", name="skills",),
        migrations.AddField(
            model_name="trainer",
            name="skills",
            field=models.ManyToManyField(to="course.skills"),
        ),
    ]