import random
import time
import json
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import get_template
from django.db.utils import IntegrityError
from product_comment.models import ProductComment, Product, SplitComment, LTPComment, UntreatedProductURL, CharacterWords, SatisfactionModel

# Create your views here.


def index(request):
    template = get_template('home.html')
    html = template.render(locals())
    return HttpResponse(html)


def home(request):
    template = get_template('index.html')
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 4)  # 每页显示两个
    page = request.GET.get('page')
    try:
        product_list = paginator.page(page)
    except PageNotAnInteger:
        product_list = paginator.page(1)
    except EmptyPage:
        product_list = paginator.paginator(paginator.num_pages)
    erro = False
    html = template.render(locals())
    return HttpResponse(html)


# 获取各评分的数量
def get_rating(id):
    rating_dict = {}
    comments = ProductComment.objects.filter(product_index_id_id=str(id))
    for record in comments:
        if rating_dict.get(record.product_rating, None):
            rating_dict[record.product_rating] += 1
        else:
            rating_dict[record.product_rating] = 1
    return rating_dict


# 获取关键词频率
def get_word_count(id):
    word_dict = {}
    split = SplitComment.objects.filter(product_index_id_id=str(id))
    with open('static/countwords.csv', 'w', encoding='utf-8') as f:
        for record in split:
            if word_dict.get(record.split_word, None):
                word_dict[record.split_word] += 1
            else:
                word_dict[record.split_word] = 1
        word_list = sorted(word_dict.items(),
                           key=lambda asd: asd[1], reverse=True)  # 按频率降序
        f.write("id,value\n")
        f.write("f,\n")
        count = 4
        end = 0
        for i in range(count):
            f.write("f.{},\n".format(i))
            gap = random.randint(12, 28)
            start = end
            end = start + gap
            for item in word_list[start:end]:
                f.write("f.{}.{},{}\n".format(i, item[0], str(item[1])))
        f.write("f.{}.{},{}".format(
            count - 1, word_list[end][0], str(word_list[end][1])))


# 获取特征词
def get_character_word(id):
    character_words = CharacterWords.objects.filter(
        product_index_id_id=str(id)).exclude(sentiment_value__isnull=True)
    # list_num = 40 if len(character_words) else len(character_words)
    list_num = len(character_words)
    cword = json.dumps(
        [cw.character_word for cw in character_words[:list_num]])
    cvalue = json.dumps(
        [cw.sentiment_value for cw in character_words[:list_num]])
    return (cword, cvalue)


# 获取满意度指标
def get_satisfaction(id):
    sword = []
    svalue = []
    satifaction_index_list = SatisfactionModel.objects.filter(
        product_index_id_id=str(id))
    for satifaction_index in satifaction_index_list:
        sword.append(satifaction_index.satisfaction_index)
        sword_value = 0
        sword_count = 0
        if satifaction_index.character_word_1:
            sword_count += 1
            character_word_object = CharacterWords.objects.filter(
                character_word=str(satifaction_index.character_word_1).split("-")[-1]).filter(product_index_id_id=str(id))[0]
            sword_value += character_word_object.sentiment_value
        if satifaction_index.character_word_2:
            sword_count += 1
            character_word_object = CharacterWords.objects.filter(
                character_word=str(satifaction_index.character_word_2).split("-")[-1]).filter(product_index_id_id=str(id))[0]
            sword_value += character_word_object.sentiment_value
        if satifaction_index.character_word_3:
            sword_count += 1
            character_word_object = CharacterWords.objects.filter(
                character_word=str(satifaction_index.character_word_3).split("-")[-1]).filter(product_index_id_id=str(id))[0]
            sword_value += character_word_object.sentiment_value
        if satifaction_index.character_word_4:
            sword_count += 1
            character_word_object = CharacterWords.objects.filter(
                character_word=str(satifaction_index.character_word_4).split("-")[-1]).filter(product_index_id_id=str(id))[0]
            sword_value += character_word_object.sentiment_value
        if satifaction_index.character_word_5:
            sword_count += 1
            character_word_object = CharacterWords.objects.filter(
                character_word=str(satifaction_index.character_word_5).split("-")[-1]).filter(product_index_id_id=str(id))[0]
            sword_value += character_word_object.sentiment_value
        satisfaction_value_result = round(sword_value / sword_count, 2)
        SatisfactionModel.objects.filter(id=satifaction_index.id).update(
            satisfaction_value=satisfaction_value_result)
        svalue.append(satisfaction_value_result)
    sword = json.dumps(sword)
    svalue = json.dumps(svalue)
    return (sword, svalue)


def detail(request, id):
    try:
        product = Product.objects.get(id=str(id))
    except Product.DoesNotExist:
        raise Http404
    if product.have_data == "是":
        # 获取各评分的数量
        rating_dict = get_rating(id)

        # 获取关键词频率
        get_word_count(id)

        # 获取特征词
        character_word = get_character_word(id)
        cword = character_word[0]
        cvalue = character_word[1]

        # 获取满意度指标
        get_satisfaction_value = get_satisfaction(id)
        sword = get_satisfaction_value[0]
        svalue = get_satisfaction_value[1]

        template = get_template('detail.html')
        html = template.render(locals())
        return HttpResponse(html)
    else:
        template = get_template('default.html')
        html = template.render(locals())
        return HttpResponse(html)


# 按标签分类
def search_tag(request, tag):
    try:
        product_list = Product.objects.filter(product_category__iexact=tag)
    except Product.DoesNotExist:
        raise Http404
    template = get_template('tag.html')
    html = template.render(locals())
    return HttpResponse(html)


# 按商品名字搜索
def product_search(request):
    template = get_template('index.html')
    if 'product_name' in request.GET:
        product_name = request.GET['product_name']
        if not product_name:
            html = template.render(locals())
            return HttpResponse(html)
        else:
            product_list = Product.objects.filter(
                product_name__icontains=product_name)
            if product_list:
                erro = False
            else:
                erro = True
            html = template.render(locals())
            return HttpResponse(html)
    return redirect('/index/')


# 提交还没有数据的商品信息
def submit_untreated_product(request):
    if 'untreated_product_url' in request.GET:
        untreated_product_url = request.GET['untreated_product_url']
        if not untreated_product_url:
            template = get_template('home.html')
            html = template.render(locals())
            return HttpResponse(html)
        else:
            untreated_product = UntreatedProductURL()
            untreated_product.untreated_product_url = untreated_product_url
            untreated_product.date_time = time.strftime("%Y-%m-%d %H:%M:%S")
            untreated_product.treated = "否"
            try:
                untreated_product.save()
            except IntegrityError:
                pass
            template = get_template('submit.html')
            html = template.render(locals())
            return HttpResponse(html)
    return redirect('/')
