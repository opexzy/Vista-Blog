"""File Model class"""
from django.db import models
from .filetypes import FileTypeModel as FileType
"""Custom File Model Manager"""
class FileModelManager(models.Manager):
    def addWaterMark(self):
        return
    def autoGenerateUrl(self):
        return

"""File Model Class"""
class FileModel(models.Model):
    name = models.CharField(max_length=250)
    file_type = models.ForeignKey(FileType, on_delete=models.CASCADE)
    file_url = models.CharField(max_length=1000)

    class Meta:
        db_table = 'files'
        indexes = [
            models.Index(fields=['name','file_type'],name="file_index")
        ]