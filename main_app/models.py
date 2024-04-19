from django.db import models
from django.urls import reverse
# Create your models here


FEATUREDEVENTS = ( #Data in this tuple should look like this ('COM', 'Comic Con') 
    ('TcN', 'TwitchCon, San Diego Convention Center, San Diego CA'), # https://www.twitchcon.com/san-diego-2024/  Date (September 20-22 2024)
    ('CcN', 'Comic-Con, San Diego Convention Center, San Diego CA'), # https://www.comic-con.org/cc/  Date (July 25-28 2024)
    ('NYc', 'New York Comic-Con, Javits Center, NYC NY'), # https://www.newyorkcomiccon.com/en-us.html  Date (October 17-20 2024)
)





class Tasks(models.Model):
    name = models.CharField(max_length=50),
    description = models.TextField(max_length=200),# Image needs a default image
    image_url = models.CharField(max_length=150, default='')
    

    
class FeaturedEvents(models.Model):
    description = models.TextField(max_length=200),# Image needs a default image
    image_url = models.CharField(max_length=150, default=''), 
    featuredEvents =models.CharField(
        max_length=150,
            choices= FEATUREDEVENTS
    )

    

    
    
     