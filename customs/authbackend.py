"""The Custom Authentication Backend"""
from django.conf import settings
from user.models.logins import LoginModel

class AuthBackend(object):
    def authenticate(self, email, password):
        #fetch data from login model
        try:
            user = LoginModel.manage.get(email=email)
            if user.check_password(password):
                return user
            else:
                return None
        except LoginModel.DoesNotExist:
            #user does not exist
            return None
        except Exception as e:
            return None
    
    def get_user(self, user_id):
        try:
            return LoginModel.manage.get(pk=user_id)
        except LoginModel.DoesNotExist:
            return None
