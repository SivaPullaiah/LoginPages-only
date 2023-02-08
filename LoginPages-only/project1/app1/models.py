from django.db import models
from datetime import *




class Blog(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    desc=models.TextField()
    author=models.CharField(max_length=100)
    created = models.DateTimeField(default=datetime.now)
    def __str__(self) -> str:
        return self.title
# Create your models here.
