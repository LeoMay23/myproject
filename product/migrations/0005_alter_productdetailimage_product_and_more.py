# Generated by Django 4.2.16 on 2024-12-04 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0004_alter_productdetail_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productdetailimage",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="product.product",
            ),
        ),
        migrations.AlterField(
            model_name="productkeyword",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="keywords",
                to="product.product",
            ),
        ),
    ]
