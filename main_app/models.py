from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here


FEATUREDEVENTS = ( #Data in this tuple should look like this ('CcN', 'Comic Con, venue, city / state') 
    ('NjH', 'New Orleans Jazz Festival, Fair Grounds Race Course & Slots, New Orleans LA'), # https://www.nojazzfest.com Date (April 25-28 & May 2-5 2024)
    ('F1M', 'F1 Crypto.com Miami Grand Prix, Miami FL'), # https://f1miamigp.com Date (May 3-5 2024)
    ('BnO', 'Bonnaroo Music Festival, Manchester TN'), # https://www.bonnaroo.com Date (June 13-16 2024)
    ('CcN', 'Comic-Con, San Diego Convention Center, San Diego CA'), # https://www.comic-con.org/cc/  Date (July 25-28 2024)
    ('LoL', 'Lollapalooza, Grant Park, Chicago IL'), # https://www.lollapalooza.com Date (Aug 1-4 2024)
    ('BmF', 'Burning Man Festival, Black Rock Desert, NV'), # https://burningman.org/event/ Date (Aug-25 Sept-2 2024)
    ('TcN', 'TwitchCon, San Diego Convention Center, San Diego CA'), # https://www.twitchcon.com/san-diego-2024/  Date (Sept 20-22 2024)
    ('NYc', 'New York Comic-Con, Javits Center, NYC NY'), # https://www.newyorkcomiccon.com/en-us.html  Date (Oct  17-20 2024)
    ('NFR', 'National Finals Rodeo, Thomas & Mack Center, Las Vegas NV'), # https://www.nfrexperience.com Date (Dec 5-14 2024)
    ('SfF', 'Sundance Film Festival, Park City UT'), # https://www.parkcity.org/departments/special-events-facilities/sundance-film-festival Date (Jan 23- Feb 2 2025)
)





class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)# Image needs a default image
    image_url = models.CharField(max_length=150, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
class FeaturedEvent(models.Model):
    description = models.TextField(max_length=200)# Image needs a default image
    image_url = models.CharField(max_length=150, default='') 
    featuredEvents =models.CharField(
        max_length=150,
        choices= FEATUREDEVENTS
            
    )

    

    
    
     