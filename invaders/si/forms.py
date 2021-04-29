from django.forms import ModelForm
from .models import City, Invader

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name', 'country', 'prefix']

class InvaderForm(ModelForm):
    class Meta:
        model = Invader
        fields = ['name', 'points', 'status', 'cp', 'city', 'comment', 'localisation', 'gmaps_url', 'latitude', 'longitude', 'flashed_by']
