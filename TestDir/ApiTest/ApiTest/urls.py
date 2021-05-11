"""ApiTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path

from Myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/',views.welcome),
    path('homea/',views.homea),
    path('home/',views.home),#--首页--
    re_path(r"^child/(?P<eid>.+)/(?P<oid>.*)/$",views.child),# 子页面映射
    path('login/',views.login),# --登录页面--
    path('login_action/',views.login_action),# --验证登录账号密码--
    path('register_action/',views.register_action),# --注册账号--
    path('accounts/login/',views.login),#--登录页面--
    path('logout/',views.logout),#--退出--
    path('pei/',views.pei),#--吐槽--
    path('help/',views.help),# --进入帮助文档
    path('project_list/',views.project_list),#项目列表
    path('delete_project/',views.delete_project),#删除项目
    path('add_project/',views.add_project),# 新增项目
    re_path(r'^apis/(?P<id>.*)/$',views.open_apis), # 进入接口库
    re_path(r'^cases/(?P<id>.*)/$',views.open_cases), # 进入用例设置
    re_path(r'^project_set/(?P<id>.*)/$',views.open_project_set), # 进入项目设置
    re_path(r'^save_project_set/(?P<id>.*)/$',views.save_project_set),# 项目设置-保存
    re_path(r'^project_api_add/(?P<Pid>.*)/$',views.project_api_add),#接口库-新增接口
    re_path(r'^project_api_del/(?P<id>.*)/$',views.project_api_del),# 接口库-删除接口
    path('save_bz/',views.save_bz),# 接口库-备注-保存
    path('get_bz/',views.get_bz),# 接口库-备注(获取备注数据)
    path('Api_save/',views.Api_save),# 接口库-调试-保存
    path('get_api_data/',views.get_api_data),# 接口库-调试（获取接口最新数据）
    path('Api_send/',views.Api_send),# seng发送请求
    path('copy_api/',views.api_id),#接口复制
    path('error_request/',views.error_request)#异常值测试-开始测试
]
