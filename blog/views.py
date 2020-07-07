from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import ModelForm
from blog.forms import PostForm
from .models import Blog
def allblogs(request):
    blogs=Blog.objects
    return render(request,'blog/allblogs.html',{'blogs':blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    print(str(detailblog.body))
    return render(request, 'blog/detail.html', {'blog':detailblog})

@login_required
def addblog(request):
    if request.user.is_superuser == 0:
        return redirect("home")

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(commit=True)
            return redirect("allblogs")

        else:
            msg="Invalid data"
            return render(request,'blog/addblog.html',{'msg':msg})



    else:
        form = PostForm()
        return render(request,'blog/addblog.html',{'form':form})
