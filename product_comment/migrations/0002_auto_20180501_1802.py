# Generated by Django 2.0.3 on 2018-05-01 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_comment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UntreatedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('untreated_product_name', models.CharField(max_length=120)),
                ('untreated_product_category', models.CharField(max_length=50)),
                ('treated', models.CharField(max_length=2)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_time'],
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='have_data',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='productcomment',
            name='comment_ltp',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='productcomment',
            name='comment_split',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterUniqueTogether(
            name='untreatedproduct',
            unique_together={('untreated_product_category', 'untreated_product_name')},
        ),
    ]
