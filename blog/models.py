from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from django.urls import reverse                                 # ADD

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):                                 # ADDED
        return reverse('post-detail', kwargs={'pk': self.pk})   # redirect to the post-detail view
                                                                #   using the new Post's pk ("primar-key")
