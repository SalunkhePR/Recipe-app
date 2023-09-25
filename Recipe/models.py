from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Recipee(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    nm=models.CharField(max_length=50)
    info=models.TextField()
    img=models.ImageField(upload_to="Recipe")