# Generated by Django 4.2.4 on 2023-08-23 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("root", "0002_rename_todo_service"),
    ]

    operations = [
        migrations.RenameField(
            model_name="service", old_name="create", new_name="created_date",
        ),
    ]