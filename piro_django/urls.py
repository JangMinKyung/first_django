"""piro_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, include
from django.shortcuts import redirect

# def root(request):
#    return redirect('blog:post_list')

urlpatterns = [
    # re_path(r'^$', root, name='root'),
    re_path(r'^$', lambda r: redirect('blog:post_list'), name='root'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^accounts/', include('accounts.urls')),
    re_path(r'^blog/', include(('blog.urls', 'blog'), namespace='blog')),
    re_path(r'^dojo/', include(('dojo.urls', 'dojo'), namespace='dojo')),
    re_path(r'^shop/', include('shop.urls')),
]
