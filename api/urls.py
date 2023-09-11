from django.urls import path, include

from api.views import GoodApiView, all_categories, ArticleGenericView, CategoryMGenericView
from .routers import router

urlpatterns = [
    path('users/', include(router.urls)),
    path('goods/', GoodApiView.as_view()),
    path('categories/', all_categories),
    path('mixin/<language>/', CategoryMGenericView.as_view()),
    path('articles/', ArticleGenericView.as_view()),
    path('articles/<int:pk>/', ArticleGenericView.as_view()),
]
              # + router.urls