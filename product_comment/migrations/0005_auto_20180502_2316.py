# Generated by Django 2.0.3 on 2018-05-02 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_comment', '0004_auto_20180501_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='SentimentDict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_value', models.FloatField(verbose_name='极值')),
                ('word', models.CharField(max_length=60, verbose_name='情感词')),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '字典管理',
                'verbose_name_plural': '字典管理',
                'ordering': ['-date_time'],
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-date_time'], 'verbose_name': '商品管理', 'verbose_name_plural': '商品管理'},
        ),
        migrations.AlterModelOptions(
            name='productcomment',
            options={'ordering': ['-date_time'], 'verbose_name': '评论详情管理', 'verbose_name_plural': '评论详情管理'},
        ),
        migrations.AlterModelOptions(
            name='untreatedproducturl',
            options={'ordering': ['-date_time'], 'verbose_name': '待处理的URL', 'verbose_name_plural': '用户提交的URL'},
        ),
        migrations.AddField(
            model_name='productcomment',
            name='comment_dict',
            field=models.CharField(max_length=2, null=True, verbose_name='是否进行字典处理'),
        ),
        migrations.AlterField(
            model_name='ltpcomment',
            name='ltp_word',
            field=models.CharField(max_length=30, verbose_name='分词'),
        ),
        migrations.AlterField(
            model_name='ltpcomment',
            name='ltp_word_id',
            field=models.CharField(max_length=5, verbose_name='分词ID'),
        ),
        migrations.AlterField(
            model_name='ltpcomment',
            name='ltp_word_parent',
            field=models.CharField(max_length=5, verbose_name='父节点的索引'),
        ),
        migrations.AlterField(
            model_name='ltpcomment',
            name='ltp_word_relate',
            field=models.CharField(max_length=6, verbose_name='关系'),
        ),
        migrations.AlterField(
            model_name='ltpcomment',
            name='product_comment_index_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_comment.ProductComment', verbose_name='评论ID'),
        ),
        migrations.AlterField(
            model_name='ltpcomment',
            name='product_index_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_comment.Product', verbose_name='商品ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='product',
            name='have_data',
            field=models.CharField(max_length=2, verbose_name='是否有此商品的数据'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.CharField(max_length=50, verbose_name='所属类别'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.CharField(max_length=30, verbose_name='商品ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=250, verbose_name='商品名称'),
        ),
        migrations.AlterField(
            model_name='productcomment',
            name='comment_ltp',
            field=models.CharField(max_length=2, verbose_name='是否依存句法分析'),
        ),
        migrations.AlterField(
            model_name='productcomment',
            name='comment_split',
            field=models.CharField(max_length=2, verbose_name='是否分词'),
        ),
        migrations.AlterField(
            model_name='productcomment',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='productcomment',
            name='product_comment',
            field=models.TextField(blank=True, null=True, verbose_name='商品评论'),
        ),
        migrations.AlterField(
            model_name='productcomment',
            name='product_index_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_comment.Product', verbose_name='商品ID'),
        ),
        migrations.AlterField(
            model_name='productcomment',
            name='product_rating',
            field=models.CharField(max_length=2, verbose_name='评分'),
        ),
        migrations.AlterField(
            model_name='splitcomment',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='splitcomment',
            name='product_index_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_comment.Product', verbose_name='商品ID'),
        ),
        migrations.AlterField(
            model_name='splitcomment',
            name='split_word',
            field=models.CharField(max_length=30, verbose_name='分词'),
        ),
        migrations.AlterField(
            model_name='untreatedproducturl',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='untreatedproducturl',
            name='treated',
            field=models.CharField(max_length=2, verbose_name='是否处理过此URL'),
        ),
        migrations.AlterField(
            model_name='untreatedproducturl',
            name='untreated_product_url',
            field=models.CharField(max_length=220, verbose_name='URL'),
        ),
        migrations.AlterUniqueTogether(
            name='sentimentdict',
            unique_together={('word',)},
        ),
    ]
