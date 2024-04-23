from django.forms import ModelForm
from .models import FeaturedEvent
from django.contrib.auth.models import User

class FeaturedEventForm(ModelForm):
  class Meta:
    model = FeaturedEvent
    fields = ['date', 'event']

