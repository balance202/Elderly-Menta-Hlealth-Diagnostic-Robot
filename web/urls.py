# -*- codeing = utf-8 -*-
# @Time:2023/9/13 23:14
# @Author:lhx
# @File:urls.py
# @Software:PyCharm
from web.views import account,home
from django.urls import path

urlpatterns = [
    path('', account.login, name='login'),
    path('web/register/', account.register, name='web_register'),
    path('login/sms/', account.login_sms, name='login_sms'),
    path('image/code/', account.image_code, name='image_code'),
    path('send/sms/', account.send_sms, name='send_sms'),
    path('logout/', account.logout, name='logout'),
    path('index/', home.index, name='index'),
    path('login/sms/', account.login_sms, name='login_sms'),
    path('login/', account.login, name='login'),
    path('image/code/', account.image_code, name='image_code'),
    path('send/sms/', account.send_sms, name='send_sms'),
    path('logout/', account.logout, name='logout'),
    path('pstest/', home.pstest, name='pstest'),
    path('datest/', home.datest, name='datest'),
    path('user/', home.user, name='user'),
    path('alert/', home.alert, name='alert'),
    path('sxt/', home.sxt, name='sxt')
]