# Generated by Django 2.0.3 on 2018-05-08 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_comment', '0011_auto_20180507_1347'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-date_time'], 'verbose_name': '商品信息管理', 'verbose_name_plural': '商品信息管理'},
        ),
        migrations.AlterModelOptions(
            name='sentimentdict',
            options={'verbose_name': '情感字典管理', 'verbose_name_plural': '情感字典管理'},
        ),
        migrations.AlterModelOptions(
            name='untreatedproducturl',
            options={'ordering': ['-date_time'], 'verbose_name': '待处理需求管理', 'verbose_name_plural': '待处理需求管理'},
        ),
        migrations.RemoveField(
            model_name='sentimentdict',
            name='date_time',
        ),
        migrations.AlterField(
            model_name='characterwords',
            name='sentiment_value',
            field=models.FloatField(blank=True, null=True, verbose_name='情感值'),
        ),
    ]
