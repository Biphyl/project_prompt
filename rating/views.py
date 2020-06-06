# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import Post,Profile,Reviews
from .forms import ProjectUpload, UpdateProfileForm
from django.contrib.auth.decorators import login_required


def home(request):
    projects = Post.objects.all()
    return render(request, 'projects/index.html',{"projects":projects})


@login_required (login_url='/accounts/login/?next=/')   
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectUpload(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('home')
    else:
        form = ProjectUpload()
        return render(request,'projects/new_post.html',{"form":form})

def search_project(request):
    
    if 'search' in request.GET and request.GET["search"]:

        search_term = request.GET.get("search")
        searched_project = Post.objects.filter(title__icontains=search_term)
        message = f"{search_term}"  
        return render(request, 'myprojects/search.html', {"message": message, "projects": searched_project})

    else:
        message = "You haven't searched for any term "
        return render(request, 'projects/search.html', {"message": message})
