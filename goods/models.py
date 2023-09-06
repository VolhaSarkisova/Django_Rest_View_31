from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Good(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category,
                                 on_delete=models.PROTECT,
                                 related_name="categories")
    price = models.FloatField(default=0)

    def __str__(self):
        return f'{self.category}: {self.name}'

    class Meta:
        verbose_name_plural = "Goods"

