from django.db import models
from django.contrib.auth.models import User
import uuid
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.CharField(max_length=255)
    body = models.TextField()
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.slug), str(self.id)])