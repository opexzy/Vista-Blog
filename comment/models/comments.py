"""Comments Model Class """
from django.db import models
from post.models.posts import PostModel as Post

"""Model Manager for Comment Model"""
class CommentModelManager(models.Manager):
    def getRootComments():
        return

"""Comment Model Class"""
class CommentModel(models.Model):
    post_id = models.ForeignKey(Post,on_delete=models.CASCADE)
    email = models.EmailField()
    display_name = models.CharField(max_length=250)
    content = models.CharField(max_length=1500)
    parent = models.BigIntegerField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    manag = CommentModelManager()

    class Meta:
        db_table = "comments"