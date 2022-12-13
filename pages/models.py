from django.db import models

# Create your models here.



class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=555, blank=True)
    body  = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name +"  -  "+ str(self.date)