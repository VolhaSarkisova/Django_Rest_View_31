from django.db import models
from django.contrib.auth.admin import User

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=250)
    content = models.TextField(max_length=3000)
    author = models.ForeignKey(User,
                               on_delete=models.PROTECT)

    def __str__(self):
        return self.name
