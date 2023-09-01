# Generated by Django 4.2.4 on 2023-09-01 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Courses",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=40)),
                ("content", models.TextField(max_length=1000)),
                ("trainer", models.CharField(max_length=50)),
                ("counted_views", models.IntegerField(default=0)),
                ("counted_like", models.IntegerField(default=0)),
                ("status", models.BooleanField(default=False)),
                ("price", models.IntegerField()),
            ],
        ),
    ]