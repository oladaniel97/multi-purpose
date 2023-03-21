from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE ,default='')
    item = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item

    class Meta:
        ordering =('-date_added',)

class Dic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE ,default='')
    id = models.IntegerField(primary_key=True)
    word = models.CharField(max_length=255,null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word
    
    class Meta:
        ordering  = ['-date_added']

class City(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE ,default='')
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


# class Userprofile(models.Model):
#     user = models.OneToOneField(User, related_name="userprofile", on_delete=models.CASCADE)
#     is_vendor = models.BooleanField(default=False)

#     def __str__(self):
#         return self.user.username

class user(models.Model):
    first_name =models.CharField(max_length =200, null = True)
    last_name =models.CharField(max_length =200, null = True)
    user_name =models.CharField(max_length =200, null = True)
    email =models.EmailField(max_length =200, null = True)
    password =models.CharField(max_length =200, null = True)
    user_id =models.BigAutoField(primary_key=True)
    date_joined =models.DateField(max_length =200, null =True)

    def __str__(self):
        return self.first_name,self.last_name 