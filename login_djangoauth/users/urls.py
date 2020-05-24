from django.conf.urls import url
from .views import RegisterView,IndexView,SendSmsView,CheckSmsView,PasswordSaveView,LoginView,CheckUserView
app_name = 'users'
urlpatterns = [
    url(r'^register/',RegisterView.as_view(),name='register'),
    url(r'^send_sms/',SendSmsView.as_view()),  # 处理static/js/jquery.js的ajax请求，请求事件：Sendpwd
    url(r'^check_sms/',CheckSmsView.as_view()), # 处理static/js/jquery.step.js的ajax请求，请求事件：$("#applyBtn").click(function(event)
    url(r'^save_psd/',PasswordSaveView.as_view()), # 处理static/js/jquery.step.js的ajax请求，请求事件：$("#submitBtn").click(function(event)
    url(r'^login/',LoginView.as_view(),name='login'),
    url(r'^check_user/',CheckUserView.as_view()),  # 处理static/js/jquery.js的ajax请求，请求事件：cliLogin
    url(r'^index/',IndexView.as_view(),name='index'),
]
