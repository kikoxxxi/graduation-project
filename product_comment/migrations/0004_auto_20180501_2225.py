# Generated by Django 2.0.3 on 2018-05-01 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_comment', '0003_auto_20180501_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=250),
        ),
    ]
