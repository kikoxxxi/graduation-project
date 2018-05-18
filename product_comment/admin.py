import random
import pymysql
from django.contrib import admin
from .models import Product, ProductComment, SplitComment, LTPComment, UntreatedProductURL, CharacterWords, SatisfactionModel, SentimentDict

# Register your models here.

MYSQL_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "880818GD/",
    "db": "product_comment_db",
    "charset": "utf8mb4",
}
admin.site.site_header = '基于商品评论的客户满意度分析管理系统'
admin.site.site_title = 'admin'


class ProductAdmin(admin.ModelAdmin):
    search_fields = ('product_name',)
    list_filter = ['product_category', 'have_data']
    # readonly_fields = ('product_id', 'date_time', 'product_category')
    list_display = ('id', 'product_id', 'product_name', 'have_data',
                    'product_category', 'date_time')
    list_display_links = ('id', 'product_id', 'product_name', 'have_data',
                          'product_category', 'date_time')


class CharacterWordsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def get_sentiment_words(self, obj):
        client = pymysql.connect(**MYSQL_CONFIG)
        cursor = client.cursor()
        product_id = obj.product_index_id_id
        character_word = obj.character_word
        query_sql = "SELECT a.ltp_word,a.product_comment_index_id_id FROM(SELECT * FROM product_comment_ltpcomment l1 WHERE l1.product_index_id_id=%s) a LEFT JOIN(SELECT * FROM product_comment_ltpcomment l2 WHERE l2.product_index_id_id=%s AND l2.ltp_word_relate='SBV') b ON a.ltp_word_id = b.ltp_word_parent AND a.product_comment_index_id_id = b.product_comment_index_id_id WHERE b.ltp_word =%s"
        cursor.execute(query_sql, (product_id, product_id, character_word))
        sentiment_words = cursor.fetchall()
        client.commit()
        client.close()
        return sentiment_words

    def get_adv_words(self, sentiment_word, sentiment_word_dict):
        client = pymysql.connect(**MYSQL_CONFIG)
        cursor = client.cursor()
        product_comment_index_id = sentiment_word[1]
        a_ltp_word = sentiment_word_dict.word
        query_sql = "SELECT b.ltp_word FROM(SELECT * FROM product_comment_ltpcomment l1 WHERE l1.product_comment_index_id_id=%s) a LEFT JOIN(SELECT * FROM product_comment_ltpcomment l2 WHERE l2.product_comment_index_id_id=%s AND l2.ltp_word_relate='ADV') b ON a.ltp_word_id = b.ltp_word_parent WHERE a.ltp_word =%s"
        cursor.execute(query_sql, (product_comment_index_id,
                                   product_comment_index_id, a_ltp_word))
        adv_words = cursor.fetchall()
        client.commit()
        client.close()
        return adv_words

    def save_model(self, request, obj, form, change):
        def make_sentiment_value(obj):
            sentiment_words = self.get_sentiment_words(obj)
            count = len(sentiment_words)
            s = 0
            for sentiment_word in sentiment_words:
                try:
                    sentiment_word_dict = SentimentDict.objects.get(
                        word=sentiment_word[0])
                except SentimentDict.DoesNotExist:
                    sentiment_word_dict = None
                if sentiment_word_dict:
                    adv_words = self.get_adv_words(
                        sentiment_word, sentiment_word_dict)
                    adv_value = 1
                    for adv_word in adv_words:
                        try:
                            adv_word_dict = SentimentDict.objects.get(
                                word=adv_word[0])
                            print(adv_word_dict.word, adv_word_dict.word_value)
                            adv_value *= adv_word_dict.word_value
                        except SentimentDict.DoesNotExist:
                            print(
                                "ADV Word {} not in sentiment dict".format(adv_word))
                    s = s + adv_value * sentiment_word_dict.word_value
                else:
                    print("Word {} not in sentiment dict".format(sentiment_word))
                    count -= 1
            try:
                result = round(s / count, 2)
            except ZeroDivisionError:
                result = 0
            print(count)
            return result

        obj.sentiment_value = make_sentiment_value(obj)
        super(CharacterWordsAdmin, self).save_model(request, obj, form, change)

    list_per_page = 10
    search_fields = ('character_word',)
    list_filter = ['product_index_id']
    readonly_fields = ('product_index_id', 'character_word',
                       'counts', 'sentiment_value')
    list_display = ('id', 'product_index_id', 'character_word',
                    'counts', 'sentiment_value')
    list_display_links = ('id', 'product_index_id', 'character_word',
                          'counts', 'sentiment_value')


class SatisfactionModelAdmin(admin.ModelAdmin):
    search_fields = ('satisfaction_index',)
    list_per_page = 30
    readonly_fields = ('satisfaction_value', )
    raw_id_fields = ("product_index_id", "character_word_1", "character_word_2",
                     "character_word_3", "character_word_4", "character_word_5")
    list_filter = ['product_index_id']
    list_display = ('id', 'product_index_id', 'satisfaction_index', 'character_word_1', 'character_word_2',
                    'character_word_3', 'character_word_4', 'character_word_5', 'satisfaction_value')
    list_display_links = ('id', 'product_index_id', 'satisfaction_index', 'character_word_1', 'character_word_2',
                          'character_word_3', 'character_word_4', 'character_word_5', 'satisfaction_value')


class UntreatedProductURLAdmin(admin.ModelAdmin):
    search_fields = ('untreated_product_url',)

    def has_add_permission(self, request):
        return False
    list_filter = ['treated']
    readonly_fields = ('untreated_product_url', 'date_time')
    list_display = ('id', 'untreated_product_url', 'treated', 'date_time')
    list_display_links = ('id', 'untreated_product_url',
                          'treated', 'date_time')


class ProductCommentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    list_filter = ['product_index_id', 'comment_ltp', 'comment_split']
    search_fields = ('product_comment',)
    list_per_page = 10
    readonly_fields = ('product_index_id', 'comment_split',
                       'comment_ltp', 'comment_dict', 'product_rating')
    list_display = ('id', 'product_index_id',
                    'product_rating',  'product_comment')
    list_display_links = ('id', 'product_index_id',
                          'product_rating', 'product_comment')


class SplitCommentAdmin(admin.ModelAdmin):
    list_filter = ['product_index_id']
    readonly_fields = ('product_index_id',)
    list_display = ('id', 'split_word')
    list_display_links = ('id', 'split_word')


class LTPCommentAdmin(admin.ModelAdmin):
    list_filter = ['product_index_id']
    readonly_fields = ('product_index_id', 'product_comment_index_id',
                       'ltp_word_id', 'ltp_word_parent', 'ltp_word_relate')
    list_display = ('id', 'ltp_word_id', 'ltp_word_parent',
                    'ltp_word', 'ltp_word_relate')
    list_display_links = ('id', 'ltp_word_id', 'ltp_word_parent',
                          'ltp_word', 'ltp_word_relate')


class SentimentDictAdmin(admin.ModelAdmin):
    list_per_page = 100
    search_fields = ('word',)
    list_display = ('id', 'word', 'word_value')
    list_display_links = ('id', 'word', 'word_value')


admin.site.register(Product, ProductAdmin)
admin.site.register(UntreatedProductURL, UntreatedProductURLAdmin)
admin.site.register(ProductComment, ProductCommentAdmin)
# admin.site.register(SplitComment, SplitCommentAdmin)
# admin.site.register(LTPComment, LTPCommentAdmin)
admin.site.register(SentimentDict, SentimentDictAdmin)
admin.site.register(CharacterWords, CharacterWordsAdmin)
admin.site.register(SatisfactionModel, SatisfactionModelAdmin)
