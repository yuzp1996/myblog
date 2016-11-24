# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import Category, Tag, Blog#这是为了让blo应用在站可编辑
# Register your models here.


class BlogAdmin(admin.ModelAdmin):#编辑admin显示的项目以及次序
    fields = [ 'title','author','content','category','tags']
    list_filter=['tags']#过滤器 根据什么可以过滤
    # list_filter=['author']
    search_fields = ['question_text']
    list_per_page=10#太好用了 后台的 显示多少条数据
admin.site.register(Blog,BlogAdmin)



admin.site.register([Category,Tag])#这也是为了让blog应用在站可编辑
