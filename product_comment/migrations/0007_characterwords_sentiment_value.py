# Generated by Django 2.0.3 on 2018-05-03 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_comment', '0006_auto_20180503_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='characterwords',
            name='sentiment_value',
            field=models.FloatField(null=True, verbose_name='情感值'),
        ),
    ]
