import datetime

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponse, redirect, reverse
from app01.models import *


# import random
# from utils.tencent.sms import send_sms_single
# from django.conf import settings

#
# def send_sms(request):
#     """ 发送短信
#         ?tpl=login  -> 548762
#         ?tpl=register -> 548760
#     """
#     tpl = request.GET.get('tpl')
#     template_id = settings.TENCENT_SMS_TEMPLATE.get(tpl)
#     if not template_id:
#         return HttpResponse('模板不存在')
#
#     code = random.randrange(1000, 9999)
#     res = send_sms_single('15131289', template_id, [code, ])
#     if res['result'] == 0:
#         return HttpResponse('成功')
#     else:
#         return HttpResponse(res['errmsg'])
#
#
# from django import forms
# from app01 import models
# from django.core.validators import RegexValidator
# from django.core.exceptions import ValidationError
#
#
# class RegisterModelForm(forms.ModelForm):
#     mobile_phone = forms.CharField(label='手机号', validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误'), ])
#     confirm_password = forms.CharField(
#         label='重复密码',
#         widget=forms.PasswordInput())
#     code = forms.CharField(
#         label='验证码',
#         widget=forms.TextInput())
#
#     class Meta:
#         model = models.UserInfo
#         fields = ['mobile_phone', 'code']
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'
#             field.widget.attrs['placeholder'] = '请输入%s' % (field.label,)


# def register(request):
#     form = RegisterModelForm()
#     return render(request, 'plogin.html', {'form': form})
#


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    elif request.method == 'POSt':

        userphone = request.POST.get('phone')
        password = request.POST.get('password')

        users = UserInfo.objects.filter(userphone=userphone)
        if users.exists():
            return HttpResponse('用户名已经存在')
        try:
            user = UserInfo()
            user.userphone = userphone
            user.password = password
            user.save()
        except:
            return HttpResponse('注册失败')

        return redirect(reverse('alogin'))


def alogin(request):
    if request.method == 'GET':
        return render(request, 'alogin.html')

    elif request.method == 'POSt':
        userphone=request.POSt('phone')
        password=request.POST('password')
        users = UserInfo.objects.filter(userphone=userphone,password=password)
        if users.exists():
            user=users.filter()
        response=redirect(reverse('index'))
        response.set_cookie('userid',user.id,expires=datetime.datetime.now()+datetime.timedelta(days=10))
        return response


def plogin(request):
    return render(request, 'plogin.html')


def index(request):
    userid=request.COOKIES.get('userid',0)
    user=UserInfo.objects.filter(id=userid).first()
    return render(request, 'index.html',{'user':user})


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
