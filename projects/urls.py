"""projects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path,include
from rest_framework import routers
from django.contrib import admin
from django.contrib.auth import views
from rating.views import PostViewset,ProfileViewset


router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewset)
router.register(r'posts', PostViewset)



urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'',include('projects.urls')),
    path('',include(router.urls)),
    path(r'accounts/', include('django_registration.backends.one_step.urls')),
    path(r'logout/', views.logout,{"next_page":'/'}),
    path(r'ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings'))
    path(r'api-auth/', include('rest+framework.url', namespace='rest_framework'))
]
