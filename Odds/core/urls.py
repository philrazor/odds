from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("" , views.home , name="home"),
    path("about/" , views.about , name="about"),
    path("contact/" , views.contact , name="contact"),
    path("login_user/" , views.login_user , name="login_user"),
    path("register_user/" , views.register_user , name="register_user"),
]