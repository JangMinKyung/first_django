from django.contrib import admin
from django.urls import re_path
from . import views
#현재 폴더에 있는 views를 임포트한다

urlpatterns = [
    re_path(r'^$', views.post_list),
    re_path(r'^(?P<id>\d+)/$', views.post_detail),

]