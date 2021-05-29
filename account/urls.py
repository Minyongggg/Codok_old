from django.urls import path
from account import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='main'),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('welcome', views.welcome, name="welcome"),
    path('logout', views.logout, name="logout"),

    path('home', views.home, name="home"),
    path('bblogin', views.bblogin, name="bblogin"),
]