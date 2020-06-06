from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path(r'',views.home,name='home'),
    path(r'newproject/', views.new_project,name='newproject'),
    path(r'search_results/', views.search_project,name="search_project"),
    path(r'update/',views.update_profile,name="profileupdate"),
    path(r'profile/', views.profile_info,name='profile')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)