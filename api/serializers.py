from rest_framework import serializers
from django.contrib.auth.admin import User
from articles.models import Article
from goods.models import Category, Good

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ['username', ]
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

