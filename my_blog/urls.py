"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from article import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^pages/$', views.pages, name='pages'),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/log/$', views.log, name='log'),
    url(r'^accounts/log/user_info/$', views.user_info, name="user_info"),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^regist/$', views.regist, name='regist'),
    url(r'^(?P<date>\d{4}-\d{2}-\d{2}.*)$', views.date, name='date'),


]

