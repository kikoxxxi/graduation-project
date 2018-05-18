# Generated by Django 2.0.3 on 2018-05-11 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_comment', '0014_delete_sentimentdict'),
    ]

    operations = [
        migrations.CreateModel(
            name='SentimentDict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_value', models.FloatField(verbose_name='极值')),
                ('word', models.CharField(max_length=255, verbose_name='情感词')),
            ],
            options={
                'verbose_name': '情感字典管理',
                'verbose_name_plural': '情感字典管理',
            },
        ),
        migrations.AlterUniqueTogether(
            name='sentimentdict',
            unique_together={('word',)},
        ),
    ]
