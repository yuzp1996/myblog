# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from blog.models import Blog,Comment
# from django.http import Http404
from blog.forms import CommentForm

import qrcode#二维码
from cStringIO import StringIO#二维码

# Create your views here.
def get_blogs(request):
    ctx = {
        'blogs': Blog.objects.all().order_by('-created')
    }
    return render(request, 'blog-list.html', ctx)


 #创建二维码
def generate_qrcode(request, data):
    img = qrcode.make(data)
     
    buf = StringIO()
    img.save(buf)
    image_stream = buf.getvalue()
     
    response = HttpResponse(image_stream, content_type="image/png")
    response['Last-Modified'] = 'Mon, 27 Apr 2015 02:05:03 GMT'
    response['Cache-Control'] = 'max-age=31536000'
    return response
     
def get_detail(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404
 
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)
 
    ctx = {
        'blog': blog,
        'comments': blog.comment_set.all().order_by('-created'),
        'form': form
    }
    return render(request, 'blog-detail.html', ctx)

def page_not_found(request,val):
    return render_to_response('404error.html',{'error':"  page_not_found"})

def page_error(request):
    return render_to_response('404error.html',{'error':"  page_error"})

def text(request):
    return render_to_response('text.html')