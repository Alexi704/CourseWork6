# Generated by Django 4.1 on 2022-08-25 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[("user", "user"), ("admin", "admin")],
                default="user",
                help_text="Выбирите роль пользователя.",
                max_length=20,
                verbose_name="Роль пользователя",
            ),
        ),
    ]
