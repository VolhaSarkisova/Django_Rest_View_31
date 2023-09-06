from django.contrib import admin
from goods.models import Good, Category

# Register your models here.
@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', )
    search_fields = ('name', )
    list_filter = ('category',)

@admin.register(Category)
class GoodAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    list_filter = ('name',)


