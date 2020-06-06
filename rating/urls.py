from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path(r'',views.home, name='home'),
]