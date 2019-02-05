from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django import forms
from.models import Post

post_list = ListView.as_view(model=Post, paginate_by=10)
post_detail = DetailView.as_view(model=Post, pk_url_kwarg='id')

post_new = CreateView.as_view(model=Post)

post_edit = UpdateView.as_view(model=Post, fields='__all__')

post_delete = DeleteView.as_view(model=Post, success_url='/blog/')