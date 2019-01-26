from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+' ,on_delete=models.CASCADE)
    # +는 포기한다는 뜻이어서 user.post_set.all() 사용 못함
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)