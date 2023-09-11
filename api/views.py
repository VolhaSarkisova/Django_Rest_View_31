from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, status
from django.contrib.auth.admin import User
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from api.serializers import UserSerializer, GoodSerializer, ArticleSerializer, CategorySerializer, CategorySerializerMixin
from articles.models import Article
from goods.models import Good, Category, Category_Mixin


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class GoodApiView(APIView):
    def get(self, request: Request):
        goods = Good.objects.all()
        serializer = GoodSerializer(goods, many=True)

        return Response(serializer.data)

@api_view(['GET',])
def all_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


class ArticleGenericView(CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)


class CategoryMGenericView(ListAPIView):
    queryset = Category_Mixin.objects.all()
    serializer_class = CategorySerializerMixin

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)