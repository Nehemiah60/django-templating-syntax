# Generated by Django 4.1.4 on 2023-01-10 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='summary',
            field=models.TextField(default='This is the thing!'),
        ),
    ]
