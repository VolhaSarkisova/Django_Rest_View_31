from django.urls import path, include

from api.views import GoodApiView, all_categories, ArticleGenericView, CategoryMixinGenericView, mixin_categories
from .routers import router

urlpatterns = [
    path('users/', include(router.urls)),
    path('goods/', GoodApiView.as_view()),
    path('categories/', all_categories),
    path('mixin/', CategoryMixinGenericView.as_view()),
    # path(r'^(?P<language>[a-z]{2})/$', mixin_categories),
    path('mix/<language>/', mixin_categories),
    path('articles/', ArticleGenericView.as_view()),
    path('articles/<int:pk>/', ArticleGenericView.as_view()),
]
              # + router.urls