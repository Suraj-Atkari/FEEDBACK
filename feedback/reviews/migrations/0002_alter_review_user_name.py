# Generated by Django 4.1.3 on 2022-11-22 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="user_name",
            field=models.CharField(max_length=50),
        ),
    ]
