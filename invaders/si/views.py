from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import City, Invader


class IndexView(generic.ListView):
    model = City

class CityView(generic.DetailView):
    model = City

class InvaderView(generic.DetailView):
    model = Invader

def update_invader(request, invader_id):
    return HttpResponse("You're updating invader %s." % invader_id)

def add_invader(request, slug):
    c = get_object_or_404(City, slug=slug)
    if c.invader_set.filter(name=request.POST['name']).count() > 0:
        return render(request, 'si/city_detail.html', {'city': c, 'error_message': 'The Invader %s already exists!' % request.POST['name']})
    i = c.invader_set.create(name=request.POST['name'])
    i.save()
    return HttpResponseRedirect(reverse('invader_detail', args=(i.slug,)))

def add_city(request):
    if City.objects.filter(name=request.POST['name']).count() > 0:
        return render(request, 'si/city_list.html', {'error_message': 'This town, %s, already exists folk!' % request.POST['name']})
    c = City(name=request.POST['name'], prefix=request.POST['prefix'])
    c.save()
    return HttpResponseRedirect(reverse('city_detail', args=(c.slug,)))