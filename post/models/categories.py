"""Categories Class Model """
from django.db import models

"""Category Model class"""
class CategoryModel(models.Model):
    name = models.CharField(max_length=150,unique=True)
    description = models.CharField(max_length=1000)

    class Meta:
        db_table = "categories"