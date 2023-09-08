from rest_framework import serializers
from django.contrib.auth.admin import User
from rest_framework.utils import json

from api.mixins import TranslatedSerializerMixin
from articles.models import Article
from goods.models import Category, Good, Category_Mixin

from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField



class CategorySerializerMixin(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Category_Mixin)
    class Meta:
        model = Category_Mixin
        fields = ['translations', ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', ]
class GoodSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Good
        fields = ['name', 'category']
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['name', 'content', 'author']

