# Generated by Django 4.1.4 on 2023-01-10 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.TextField(max_length=120),
        ),
    ]
