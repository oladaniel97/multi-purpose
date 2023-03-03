from django.db import models

# Create your models here.
class Todo(models.Model):
    item = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item

    class Meta:
        ordering =('-date_added',)

class Dic(models.Model):
    id = models.IntegerField(primary_key=True)
    word = models.CharField(max_length=255,null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word
    
    class Meta:
        ordering  = ['-date_added']

class City(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name