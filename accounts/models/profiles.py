from django.db import models
from typing import Any
from django.db.models.signals import post_save
from django.dispatch import receiver
from .users import *

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=255)
    image = models.ImageField(blank=True,null=True)
    description = models.TextField(blank=True)
    instagram_link = models.URLField(max_length=255,null=True,blank=True)
    github_link = models.URLField(max_length=255,null=True,blank=True)
    linkedin_link = models.URLField(max_length=255,null=True,blank=True)
    gmail_link = models.URLField(max_length=255,null=True,blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email


'''when user was created , An object is automatically created inside the profile '''
@receiver(post_save, sender=User)
def save_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)