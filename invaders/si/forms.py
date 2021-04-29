from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse

class City(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200)
    prefix = models.CharField(max_length=4)

    def __str__(self):
        return '{}, {}'.format(self.name, self.country)

    def create_invaders_until(self, max_number):
        for i in range(1, max_number):
            self.invader_set.create(name=self.prefix+str(i).zfill(2))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(City, self).save(*args, **kwargs)

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name', 'country', 'prefix']

class Invader(models.Model):
    STATUS = [
        (0, 'Destroyed'),
        (1, 'Non visible'),
        (2, 'Severly damaged'),
        (3, 'Damaged'),
        (4, 'Slightly damaged'),
        (5, 'OK')
    ]

    POINTS = [
        (10, '10 pts'),
        (20, '20 pts'),
        (30, '30 pts'),
        (40, '40 pts'),
        (50, '50 pts'),
        (100, '100 pts')
    ]

    name = models.CharField(max_length=8, unique=True, null=False)
    slug = models.SlugField(max_length=8, blank=True, null=True)
    points = models.PositiveIntegerField(choices=POINTS, blank=True, null=True)
    status = models.PositiveIntegerField(choices=STATUS, default=5, blank=True, null=True)
    cp = models.CharField(max_length=5, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255, blank=True, null=True)
    localisation = models.TextField(max_length=511, blank=True, null=True)
    gmaps_url = models.URLField(max_length=200, blank=True, null=True)
    latitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    flashed_by = models.ManyToManyField(User, blank=True)

    def get_absolute_url(self):
        return reverse('invader-detail', kwargs={'pk': self.pk})

class InvaderForm(ModelForm):
    class Meta:
        model = Invader
        fields = ['name', 'points', 'status', 'cp', 'city', 'comment', 'localisation', 'gmaps_url', 'latitude', 'longitude', 'flashed_by']

    def is_flashable(self):
        return self.status > 1

    def __str__(self):
        return '{} ({} {}, statut {})'.format(self.name, self.cp, self.city.name, self.status)
    
    def get_instagram_link(self):
        return 'https://www.instagram.com/explore/tags/' + self.slug + '/'

    def save(self, *args, **kwargs):
        self.name = self.name.upper().strip()
        self.slug = slugify(self.name)
        return super(Invader, self).save(*args, **kwargs)