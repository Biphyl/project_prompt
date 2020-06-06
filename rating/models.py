# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    bio = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='images/', default='images/smoke.jpeg')
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    
    
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()
     
    @classmethod   
    def update_name(cls,id,new_First_Name):
        cls.objects.filter(user_id = id).update(First_Name=new_First_Name)
        new_title_object = cls.objects.get(First_Name=new_First_Name)
        new_name = new_title_object.First_Name
        return new_name
        
    @classmethod
    def get_user_profile(cls,id):
        profile = cls.objects.get(user_id=id)
        return profile


