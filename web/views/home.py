# -*- codeing = utf-8 -*-
# @Time:2023/9/16 23:01
# @Author:lhx
# @File:home.py
# @Software:PyCharm
from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request, 'index.html')

def pstest(request):
    return render(request, 'pstest.html')


def datest(request):
    return render(request, 'datest.html')


def user(request):
    return render(request, 'user.html')


def alert(request):
    return render(request, 'alert.html')


def sxt(request):
    return render(request, 'sxt.html')
