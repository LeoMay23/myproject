# Generated by Django 4.2.16 on 2024-12-05 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="PurchasedItem",
        ),
    ]
