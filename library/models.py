from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=100, help_text="Please enter the NAME of the book and its AUTHOR!")
    content = models.TextField(max_length=1000, help_text="Enter a SUMMARY for the book!")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    book_img = models.ImageField(default='default_book.jpg', upload_to='book_images')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
""" 
class Books(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=100) """
