# Generated by Django 4.1.7 on 2023-03-21 17:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("veterinary", "0036_servicio"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Servicio",
            new_name="Services",
        ),
    ]