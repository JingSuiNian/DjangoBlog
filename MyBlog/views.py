# -*- coding: utf-8 -*-

import datetime

from django.core.context_processors import csrf
from django.shortcuts import render

from MyBlog.models import MyBlog


def index(request):
    context = {}
    context['hello'] = 'Hello World'
    return render(request, 'index.html', context)


def post(request):
    ctx = {}
    ctx.update(csrf(request))
    if request.POST:  # 请求中有POST的表单内容的话,则储存,更新ctx;如没有,则直接返回post.html
        new_blog = MyBlog(title=request.POST['title'], artical=request.POST['article'], date=datetime.datetime)
        new_blog.save()
        ctx['rlt'] = request.POST['title']
    return render(request, "post.html", ctx)
