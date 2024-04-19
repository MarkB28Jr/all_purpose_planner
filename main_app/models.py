from django.db import models

# Create your models here







class Tasks(models.Model):
    name = models.CharField(max_length=50),
    description = models.TextField(max_length=200),
    image_url = models.CharField(max_length=150)
    
class FeaturedEvents(models.Model):
    description = models.TextField(max_length=200),
    image_url = models.CharField(max_length=150),
    location = models.CharField(max_length=100) # When entering this data include  venue, city, and state
    featuredEvents =models.CharField(
        max_length=100,
            choices= FEATUREDEVENTS
    )

    

    
    
     