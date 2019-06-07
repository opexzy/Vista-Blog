from django.conf.urls import url
from .views import login, register

urlpatterns = [
    url(r'^login/$',login.LoginView.as_view(), name="login"),
    url(r'^register/$',register.RegisterView.as_view(), name="register")

]