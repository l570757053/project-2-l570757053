from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import FloatField


class User(AbstractUser):
    pass

class shangpin(models.Model):
    ID=models.BigAutoField(primary_key=True,editable=False)
    master=models.ForeignKey(User,on_delete=models.CASCADE,to_field='username',verbose_name="username")
    user=models.CharField(max_length=20)
    price=models.FloatField(max_length=20)
    content=models.CharField(max_length=100)
    kind=models.CharField(max_length=20)
    time=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=20,unique=True)
    pic=models.ImageField(null=True,upload_to='img/',verbose_name="Image")
    start=models.BooleanField(default=True)

class pinglun(models.Model):
    user=models.CharField(max_length=20)
    text=models.CharField(max_length=200)
    time=models.DateTimeField(auto_now_add=True)
    id=models.BigAutoField(primary_key=True,editable=False)
    sp=models.ForeignKey(shangpin,on_delete=models.CASCADE,to_field='name',verbose_name="name")

class shoucang(models.Model):
    id=models.BigAutoField(primary_key=True,editable=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE,to_field='username',verbose_name="username")
    sp=models.ForeignKey(shangpin,on_delete=models.CASCADE,to_field='name',verbose_name="name")
