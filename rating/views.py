# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import Post,Profile,Reviews


def home(request):
    projects = Post.objects.all()
    return render(request, 'projects/index.html',{"projects":projects})
