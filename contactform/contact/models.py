from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email =models.EmailField(blank=True,required=True)
    password = models.IntegerField(max_length=8)
    subject =models.CharField(max_length=255,required=True)
    message = models.TextField(max_length=255)


    def __str__(self):
        return self.name
