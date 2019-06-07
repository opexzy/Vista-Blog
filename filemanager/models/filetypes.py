"""File Type Model Class"""
from django.db import models

class FileTypeModel(models.Model):
    name = models.CharField(max_length=50,unique=True)
    extension = models.CharField(max_length=5,unique=True)
    max_size = models.IntegerField()
    info = models.CharField(max_length=500)

    class Meta:
        db_table = 'file_types'