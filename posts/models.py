from django.db import models

# Create your models here.
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png', null=True, blank=True)

    def _str_(self):
        return self.title