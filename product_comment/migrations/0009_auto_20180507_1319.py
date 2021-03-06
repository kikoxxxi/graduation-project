# Generated by Django 2.0.3 on 2018-05-07 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_comment', '0008_auto_20180507_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='satisfactionmodel',
            name='character_word_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='c1', to='product_comment.CharacterWords', verbose_name='特征词1'),
        ),
        migrations.AlterField(
            model_name='satisfactionmodel',
            name='character_word_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='c2', to='product_comment.CharacterWords', verbose_name='特征词2'),
        ),
        migrations.AlterField(
            model_name='satisfactionmodel',
            name='character_word_3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='c3', to='product_comment.CharacterWords', verbose_name='特征词3'),
        ),
        migrations.AlterField(
            model_name='satisfactionmodel',
            name='character_word_4',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='c4', to='product_comment.CharacterWords', verbose_name='特征词4'),
        ),
        migrations.AlterField(
            model_name='satisfactionmodel',
            name='character_word_5',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='c5', to='product_comment.CharacterWords', verbose_name='特征词5'),
        ),
    ]
