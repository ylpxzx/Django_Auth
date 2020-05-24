import random
from .tasks import send_sms
import json
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.views.generic import View
from conf.aliyun_api import AliYunSms
from django.core.cache import cache
from django.urls import reverse
from .models import *
from django.utils.decorators import method_decorator
#Django自带的加密模块
from django.contrib.auth.hashers import make_password,check_password

#Django认证、登录和登出模块
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


class RegisterView(View):
    def get(self,request):
        return render(request,'registered.html')


class IndexView(View):
    @method_decorator(login_required())
    def get(self,request):
        message = {'message': 'test'}

        return render(request,'index.html',message)


class LoginView(View):
    def get(self,request):
        return render(request,'login.html')


class CheckUserView(View):
    def get(self,request):
        return render(request, 'login.html')

    def post(self,request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print(username,password)

        user = authenticate(username=username, password=password)
        print(user)
        if user is not None and user.is_active:
            login(request, user)
            # return redirect(reverse("users:index")) # ajax是不支持重定向的，所以这行代码没有任何意义，可以通过传给前端信号来实现重定向
            ret = {"status": 20, 'msg': '登录成功'}
            return HttpResponse(json.dumps(ret))
        else:
            ret = {"status": 40, 'msg': '用户名或密码错误'}
            return HttpResponse(json.dumps(ret))


class SendSmsView(View):
    def get(self,request):
        return render(request, 'registered.html')

    def post(self,request):
        # 处理/static/js/jquery.js的ajax请求：Sendpwd(sender)
        phone_number = request.POST.get('phone','')
        print('手机号：',phone_number)
        if LoginUser.objects.filter(phone_numbers=phone_number):
            ret = {"status": 40, 'msg': '该手机号已被注册'}
            return HttpResponse(json.dumps(ret))
        else:
            code = (random.randint(1000, 100000))
            # params = "{'code':%d}" % code

            # 不采用celery方式发送短信
            # sms_obj = AliYunSms(phone_number,params)
            # print(sms_obj)
            # response = sms_obj.send()

            # 采用celery发送短信
            # send_sms.delay(phone_number,params)

            cache.set(phone_number, code, 150)
            ret = {"status": 20, 'msg': '验证码发送成功','code':code}
            return HttpResponse(json.dumps(ret))


class CheckSmsView(View):
    def get(self,request):
        return render(request, 'registered.html')

    def post(self,request):
        # 处理/static/js/jquery.step.js的ajax请求：$("#applyBtn").click
        phone_number = request.POST.get('phone','')
        code = request.POST.get('code','')
        print('手机号：',phone_number,'验证码',code)
        res = cache.get(phone_number)
        print('code值为',res)
        if code == str(res):
            ret = {"status": 20, 'msg': '验证码验证成功'}
        else:
            ret = {"status": 40, 'msg': '验证码错误或过期'}

        return HttpResponse(json.dumps(ret))


class PasswordSaveView(View):
    def get(self,request):
        return render(request, 'registered.html')

    def post(self,request):
        # 处理/static/js/jquery.step.js的ajax请求：$("#submitBtn").click
        phone_number = request.POST.get('phone','')
        password = request.POST.get('password','')
        print('手机号：',phone_number,'密码：',password)

        if LoginUser.objects.filter(phone_numbers=phone_number):
            ret = {"status": 40, 'msg': '该手机号已被注册'}
            return HttpResponse(json.dumps(ret))
        else:

            # 保存注册成功的用户数据
            user_profile = LoginUser(phone_numbers=phone_number)
            user_profile.username = phone_number
            # user_profile.is_active = False
            user_profile.password = make_password(password)
            user_profile.save()
            ret = {"status": 20, 'msg': '注册成功！'}
            return HttpResponse(json.dumps(ret))


