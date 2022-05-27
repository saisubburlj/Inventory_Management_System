from django.urls import path
from . import views

app_name = "web_app"
urlpatterns = [
    path("", views.index, name = "index"),
    path("login/<str:username>", views.login, name = "login"),
    path("welcome/", views.welcome, name = "welcome")
]