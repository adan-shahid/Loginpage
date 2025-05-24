from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('login/', views.loginPage, name="login"),
    path('signup/', views.signupPage, name="signup"),
]