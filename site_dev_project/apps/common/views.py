#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017/04/28
@author: oliver
Common模块View业务处理。
"""

from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from .models import *
import json
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.hashers import make_password

# 首页



def global_setting(request):
    # 友情链接数据
    links_list = Links.objects.all()
    # 广告列表
    ad_list = Ad.objects.all()
    # 课程列表最新
    courses_list = getPage(request, Course.objects.all(), 8)
    # 课程列表最多播放量
    student_count_list = getPage(request, Course.objects.all().order_by('-student_count'), 8)
    # 课程列表最具人气
    click_count_list = getPage(request, Course.objects.all().order_by('-click_count'), 8)

    #个人导航栏
    person_nav_list = Person_nav.objects.all()
    return locals()


def index(request):

    return render(request, "common/index.html", locals())


# 搜索

def search(request):
    dat = request.GET['word']

    # key_list = Keywords.objects.filter(name__contains=dat)  # exact
    course_list = Course.objects.filter(name__contains=dat)
    course_list_json = serialize('json', course_list)

    return HttpResponse(json.dumps(course_list_json), content_type='application/json')


# 分页代码
def getPage(request, article_list, page):
    total = len(article_list)
    totalPage = 0
    if (total / page == 0):
        totalPage = total / page
    else:
        totalPage = total / page + 1

    pageList = []
    paginator = Paginator(article_list, page)
    for p in range(1, totalPage + 1):
        pageList.append([])
        pageList[p - 1] = paginator.page(p)

    return pageList

    # paginator = Paginator(article_list, 8)
    # try:
    #     page = int(request.GET.get('page', 1))
    #     article_list = paginator.page(page)
    # except (EmptyPage, InvalidPage, PageNotAnInteger):
    #     article_list = paginator.page(1)
    # return article_list


#职业课程
def careercourse(request):
    careercourse_list = getPage(request, CareerCourse.objects.all(), 9)

    return render(request, 'common/wheat.html', locals())


#详细课程
def detailcourse(request):
    return render(request, 'common/courseplay.html', locals())


#老师
def teacher(request):
    return render(request, 'common/teacher.html', locals())



#登陆
def login(request):
    return render(request, 'common/login.html', locals())

#学生个人中心
def myinformation(request):
    return render(request, 'student/person_center_information.html', locals())

def mycourse(request):
    return render(request, 'student/person_center_course.html', locals())

def mycollect(request):
    return render(request, 'student/person_center_collect.html', locals())

def mycertificate(request):
    return render(request, 'student/person_center_certificate.html', locals())

def mymessage(request):
    return render(request, 'student/person_center_message.html', locals())



#注销
def do_logout(request):
    try:
        logout(request)
    except Exception as e:
        pass
    return redirect(request.META['HTTP_REFERER'])

# 注册
# def do_reg(request):
#     try:
#         if request.method == 'POST':
#             reg_form = RegForm(request.POST)
#             if reg_form.is_valid():
#                 # 注册
#                 user = User.objects.create(username=reg_form.cleaned_data["username"],
#                                     email=reg_form.cleaned_data["email"],
#                                     url=reg_form.cleaned_data["url"],
#                                     password=make_password(reg_form.cleaned_data["password"]),)
#                 user.save()
#
#                 # 登录
#                 user.backend = 'django.contrib.auth.backends.ModelBackend' # 指定默认的登录验证方式
#                 login(request, user)
#                 return redirect(request.POST.get('source_url'))
#             else:
#                 return render(request, 'failure.html', {'reason': reg_form.errors})
#         else:
#             reg_form = RegForm()
#     except Exception as e:
#         pass
#     return render(request, 'reg.html', locals())
#
#
#
# #登录
# def do_login(request):
#     try:
#         if request.method == 'POST':
#             login_form = LoginForm(request.POST)
#             if login_form.is_valid():
#                 # 登录
#                 username = login_form.cleaned_data["username"]
#                 password = login_form.cleaned_data["password"]
#                 user = authenticate(username=username, password=password)
#                 if user is not None:
#                     user.backend = 'django.contrib.auth.backends.ModelBackend' # 指定默认的登录验证方式
#                     login(request, user)
#                 else:
#                     return render(request, 'failure.html', {'reason': '登录验证失败'})
#                 return redirect(request.POST.get('source_url'))
#             else:
#                 return render(request, 'failure.html', {'reason': login_form.errors})
#         else:
#             login_form = LoginForm()
#     except Exception as e:
#         pass
#     return render(request, 'login.html', locals())