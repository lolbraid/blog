from django.urls import path
from . import views
from .views import PasswordsChange, profile
from django.contrib.auth.views import LoginView, LogoutView

import random
cho = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y,','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*']
p = random.choices(cho, k=9)
up = random.choices(cho, k=9)
def lts(s):  
    str1 = ""
    for ele in s:  
        str1 += ele   
    return str1
slug = lts(p)
slug = lts(up)

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    # path('profile/', views.profile, name='profile'),
    path('<int:pk>/profile/', profile.as_view(), name='profile'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path('password/', PasswordsChange.as_view()),
    path('pass_succ/', views.pass_succ, name = 'pass_succ'),
]