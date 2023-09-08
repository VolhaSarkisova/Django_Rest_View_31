from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, status
from django.contrib.auth.admin import User
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from api.serializers import UserSerializer, GoodSerializer, ArticleSerializer, CategorySerializer, CategorySerializerMixin
from articles.models import Article
from goods.models import Good, Category, Category_Mixin
from django.utils import translation
from django.conf import settings

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
class CategoryMixinGenericView( CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Category_Mixin.objects.all()
    serializer_class = CategorySerializerMixin

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)
    # def get(self, request: Request):
    #     categories_maxin = Category_Mixin.objects.all()
    #     serializer = CategorySerializerMixin(categories_maxin, many=True)
    #
    #     return Response(serializer.data)
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


@api_view(['GET',])
def mixin_categories(request: Request, language):
    categories = Category_Mixin.objects.all()
    serializer = CategorySerializerMixin(categories, many=True)

    # url = request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
    url = request.META['PATH_INFO']
    print(request.META['PATH_INFO'])
    return Response(serializer.data+[url], status=status.HTTP_201_CREATED)


class ArticleGenericView(CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)
