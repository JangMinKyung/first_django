from django.contrib import admin
from django.urls import re_path
from blog import views_cbv
from . import views
#현재 폴더에 있는 views를 임포트한다

app_name = 'blog'

urlpatterns = [
    re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    re_path(r'^cbv/new/$', views_cbv.post_new),
]