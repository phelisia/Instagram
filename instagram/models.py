from django.db import models
from django.utils import timezone
from datetime import datetime


# Create your models here.
class Image(models.Model):
    image = models.ImageField(blank=True,null=True)
    imagename=models.TextField()
    caption=models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    comments= models.TextField()
    


    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()


class Profile(models.Model):
    profile_photo=models.ImageField(blank=True,null=True)
    bio=models.TextField()
    profilename=models.TextField()

    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.name


    