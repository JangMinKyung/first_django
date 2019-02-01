# blog/models.py
import re
from django.urls import reverse
from django.forms import ValidationError
from django.db import models
from django.conf import settings

# Create your models here.

def lnglat_validator(value):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.CharField(max_length=20, blank=True)
    title = models.CharField(max_length=100, verbose_name='제목',
                            help_text='제목을 입력해주세요. 최대 100자 내외.') # 길이 재한이있는 문자열
    content = models.TextField(verbose_name='내용') # 길이 재한이 없는 문자열
    photo = models.ImageField(blank=True, upload_to='blog/post/%Y/%m/%d')
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50,
                              help_text='경도/위도 포맷으로 입력',
                              blank=True,
                              validators=[lnglat_validator]
                              )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

