from django.forms import ModelForm
from .models import FeaturedEvent

class FeaturedEventForm(ModelForm):
  class Meta:
    model = FeaturedEvent
    fields = ['date', 'event']