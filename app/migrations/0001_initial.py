# Generated by Django 4.1.4 on 2023-02-17 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="student",
            fields=[
                ("st_id", models.IntegerField(primary_key=True, serialize=False)),
                ("st_name", models.CharField(max_length=100)),
                ("st_age", models.IntegerField()),
            ],
        ),
    ]
