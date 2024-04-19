from django.db import models

# Create your models here







class Tasks(models.Model):
    name = models.CharField(max_length=50),
    description = models.TextField(max_length=200),
    image_url = models.CharField(max_length=150)
    

    

    
    
     