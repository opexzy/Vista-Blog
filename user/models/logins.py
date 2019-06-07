""" Login Model Class Definition for the user app """
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

# Acceptable gender for users
GENDER = (
    ('M','Male'),
    ('F','Female'),
)
# Valid user type for users
USER_TYPE = (
    (1,'Administrator'),
    (2,'Moderator'),
    (3,'Author'),
)
# Valid user status
STATUS = (
    (0,'Inactive'),
    (1,'Active'),
)
"""Model Manager for User Model"""
class UserModelManager(BaseUserManager):

    def create_user(self,email,password, **more_fields):
        #create and a save a user
        if not email:
            raise ValueError('Users Must Provide a valid Email')
        user = self.model(email=self.normalize_email(email),**more_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **more_fields):
        user = self.create_user(email,password,**more_fields)
        user.user_type = 1
        user.status = 1
        user.save(using=self._db)
        return user

    def add_new_user(self, email, password, **kwargs):
        #check if email exist alredy in the database
        try:
            user = self.model.manage.get(email=self.normalize_email(email))
            return False
        except self.model.DoesNotExist:
            #add new user to database
            user = self.model(email=self.normalize_email(email),**kwargs)
            user.set_password(password)
            user.save(using=self._db)
            return True
            
    def getFullName(self):
        # Block
        return
""" User Model """
class LoginModel(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50,default='unset')
    last_name = models.CharField(max_length=50,default='unset')
    email = models.EmailField(unique=True)
    gender = models.CharField(choices=GENDER,max_length=1)
    user_type = models.IntegerField(choices=USER_TYPE,default=3)
    status = models.IntegerField(choices=STATUS,default=0)
    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    manage = UserModelManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "logins"

    def __str__(self):
        return self.email