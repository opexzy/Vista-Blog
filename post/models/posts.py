""" Post Model class definition """
from django.db import models
from .categories import CategoryModel as PostCategory
from user.models.logins import LoginModel as Author
# options for post status
STATUS = (
    (2,'Approved'),
    (1, 'Disapproved'),
    (0,'Trash'),
)
# options for post flags
FLAGS = (
    ('N','Normal Post'),
    ('F','Front Page Post'),
)

"""Creates Slug from Post Title"""
def slug(title):
        #Create slug from post title
        return

# Model Manager for Post Model
class PostModelManager(models.Manager):
    def getslug(self,title=None):
        #slug utitlity for model manager
        return

class PostModel(models.Model):
    title = models.CharField(max_length=350)
    slug = models.CharField(max_length=700)
    category = models.ForeignKey(PostCategory, on_delete = models.CASCADE)
    content = models.TextField
    status = models.IntegerField(choices=STATUS)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    views = models.BigIntegerField(default=0)
    flag = models.CharField(max_length=1,choices=FLAGS,default='N')
    flag_raised_on = models.DateTimeField(auto_now=True)
    manage = PostModelManager()

    class Meta:
        db_table = 'posts'