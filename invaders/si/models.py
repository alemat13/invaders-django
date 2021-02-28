from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    prefix = models.CharField(max_length=4)

    def __str__(self):
        return '{}, {}'.format(self.name, self.country)


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

    name = models.CharField(max_length=8, unique=True)
    points = models.PositiveIntegerField(choices=POINTS)
    status = models.PositiveIntegerField(choices=STATUS, default=5)
    cp = models.CharField(max_length=5, required=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255, required=False)
    localisation = models.TextField(max_length=511, required=False)
    gmaps_url = models.URLField(max_length=200, required=False)
    latitude = models.DecimalField(max_digits=11, decimal_places=8, required=False)
    longitute = models.DecimalField(max_digits=11, decimal_places=8, required=False)
    flashed_by = models.ManyToManyField(User)

    def is_flashable(self):
        return self.status > 1

    def __str__(self):
        return '{} ({} {}, statut {})'.format(self.name, self.cp, self.city.name, self.status)
    
    def get_instagram_link(self):
        base_url = 'https://www.instagram.com/explore/tags/' + self.name.lower() + '/'

