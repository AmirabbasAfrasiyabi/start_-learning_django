from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
class Post(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    view_count = models.PositiveIntegerField(default=0)
    like_count = models.PositiveIntegerField(default=0)