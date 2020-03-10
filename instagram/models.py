from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    profile_photo=models.ImageField(upload_to='images/')
    bio=models.TextField()
    profilename=models.TextField()

    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.name

class Image(models.Model):
    author = models.ForeignKey(Profile,null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    image_name=models.TextField()
    caption=models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    


    def __str__(self):
        return self.caption

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

class Comment(models.Model):
    post = models.ForeignKey(Image, on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)


    