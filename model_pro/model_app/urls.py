from django.urls import path
from model_app import views


app_name='model_app'

urlpatterns=[
    path("register/",views.register,name="register"),
    path("user_login/",views.user_login,name="user_login")
]