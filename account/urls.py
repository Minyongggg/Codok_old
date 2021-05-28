from django.urls import path
from account import views 

urlpatterns = [
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('logout', views.logout, name="logout"),

    path('', views.home, name="home"),
    path('bblogin', views.bblogin, name="bblogin"),
]