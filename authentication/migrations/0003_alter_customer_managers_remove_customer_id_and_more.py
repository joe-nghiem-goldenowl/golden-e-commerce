# Generated by Django 4.2.7 on 2023-11-13 03:10

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("authentication", "0002_alter_customer_table"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="customer",
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name="customer",
            name="id",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="user",
        ),
        migrations.AddField(
            model_name="customer",
            name="user_ptr",
            field=models.OneToOneField(
                auto_created=True,
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
