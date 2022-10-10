from django.db import models

# Create your models here.


class Messages(models.Model):
     name = models.CharField(max_length=1000, null=True, blank=True)
     email  = models.CharField(max_length=100, null=True, blank=True)
     subject = models.CharField(max_length=100, null=True, blank=True)
     lll = models.CharField(max_length=100, null=True, blank=True)
     message = models.TextField(null=True, blank=True)

     def __str__(self):
         return self.subject
     


    