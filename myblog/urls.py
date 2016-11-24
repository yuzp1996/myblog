"""myblog URL Configuration

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
from blog.views import get_blogs,get_detail,text,generate_qrcode

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^blog/$',get_blogs),
    url(r'^blog$', get_blogs, name='blog_get_blogs'),
    url(r'^detail/(\d+)/$', get_detail, name='blog_get_detail'),
    url(r'^text$',text),
    url(r'^qrcode/(.+)$', generate_qrcode, name='qrcode'),
]
handler404 = 'blog.views.page_not_found'
handler500 = 'blog.views.page_error'
handler400 = 'blog.views.page_not_found'
