from django.db import models

# Create your models here.


class Product(models.Model):
    product_id = models.CharField(max_length=255, verbose_name='商品ID')
    product_name = models.CharField(max_length=255, verbose_name='商品名称')
    product_category = models.CharField(max_length=255, verbose_name='所属类别')
    have_data = models.CharField(max_length=255, verbose_name='是否有此商品的特征词')
    date_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    def __str__(self):
        return "{}-{}".format(self.id, self.product_name)

    class Meta:
        ordering = ['-date_time']
        unique_together = ['product_id', 'product_name']
        verbose_name = '商品信息管理'
        verbose_name_plural = '商品信息管理'


class CharacterWords(models.Model):
    product_index_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='商品ID')
    character_word = models.CharField(max_length=255, verbose_name='特征词')
    sentiment_value = models.FloatField(
        verbose_name='情感值', null=True, blank=True)
    counts = models.IntegerField(verbose_name='频率')

    def __str__(self):
        return "{}-{}".format(self.product_index_id, self.character_word)

    class Meta:
        ordering = ['-product_index_id', '-counts']
        unique_together = ['product_index_id', 'character_word']
        verbose_name = '特征词管理'
        verbose_name_plural = '特征词管理'


class SatisfactionModel(models.Model):
    product_index_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='商品ID', null=True)
    satisfaction_index = models.CharField(
        max_length=255, verbose_name='满意度指标')
    character_word_1 = models.ForeignKey(
        CharacterWords, on_delete=models.CASCADE, related_name='c1', verbose_name='特征词1', null=True, blank=True)
    character_word_2 = models.ForeignKey(
        CharacterWords, on_delete=models.CASCADE, related_name='c2', verbose_name='特征词2', null=True, blank=True)
    character_word_3 = models.ForeignKey(
        CharacterWords, on_delete=models.CASCADE, related_name='c3', verbose_name='特征词3', null=True, blank=True)
    character_word_4 = models.ForeignKey(
        CharacterWords, on_delete=models.CASCADE, related_name='c4', verbose_name='特征词4', null=True, blank=True)
    character_word_5 = models.ForeignKey(
        CharacterWords, on_delete=models.CASCADE, related_name='c5', verbose_name='特征词5', null=True, blank=True)
    satisfaction_value = models.FloatField(
        verbose_name='满意度', null=True, blank=True)

    def __str__(self):
        return "{}-{}".format(self.product_index_id, self.satisfaction_index)

    class Meta:
        ordering = ['-product_index_id', ]
        unique_together = ['product_index_id', 'satisfaction_index']
        verbose_name = '满意度模型管理'
        verbose_name_plural = '满意度模型管理'


class UntreatedProductURL(models.Model):
    untreated_product_url = models.CharField(
        max_length=255, verbose_name='URL')
    treated = models.CharField(max_length=255, verbose_name='是否处理过此URL')
    date_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    def __str__(self):
        return "{}".format(self.untreated_product_url)

    class Meta:
        ordering = ['-date_time']
        unique_together = ['untreated_product_url']
        verbose_name = '待处理需求管理'
        verbose_name_plural = '待处理需求管理'


class ProductComment(models.Model):
    product_index_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='商品ID')
    product_comment = models.TextField(
        null=True, blank=True, verbose_name='商品评论')
    product_rating = models.CharField(max_length=255, verbose_name='评分')
    comment_split = models.CharField(max_length=255, verbose_name='是否分词')
    comment_ltp = models.CharField(max_length=255, verbose_name='是否依存句法分析')
    comment_dict = models.CharField(
        max_length=255, null=True, verbose_name='是否进行字典处理')
    date_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        ordering = ['-date_time']
        verbose_name = '评论详情管理'
        verbose_name_plural = '评论详情管理'


class SentimentDict(models.Model):
    word_value = models.FloatField(verbose_name='极值')
    word = models.CharField(max_length=255, verbose_name='情感词')

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        unique_together = ['word']
        verbose_name = '情感字典管理'
        verbose_name_plural = '情感字典管理'


class SplitComment(models.Model):
    product_index_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='商品ID')
    split_word = models.CharField(max_length=255, verbose_name='分词')
    date_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        ordering = ['-date_time']
        verbose_name = '分词管理'
        verbose_name_plural = '分词管理'


class LTPComment(models.Model):
    product_index_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='商品ID')
    product_comment_index_id = models.ForeignKey(
        ProductComment, on_delete=models.CASCADE, verbose_name='评论ID')
    ltp_word_id = models.CharField(max_length=255, verbose_name='分词ID')
    ltp_word = models.CharField(max_length=255, verbose_name='分词')
    ltp_word_relate = models.CharField(max_length=255, verbose_name='关系')
    ltp_word_parent = models.CharField(max_length=255, verbose_name='父节点的索引')

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        ordering = ['-product_index_id']
        verbose_name = '依存句法分析结果管理'
        verbose_name_plural = '依存句法分析结果管理'
