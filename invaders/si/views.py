from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import City, Invader

def index(request):
    return HttpResponse("Hello world, your in SI index.")

def city(request, city_id):
    c = get_object_or_404(City, pk=city_id)
    return render(
        request,
        'si/city.html',
        {'city': c}
    )

def invader_detail(request, invader_id):
    i = get_object_or_404(Invader, pk=invader_id)
    return render(
        request,
        'si/invader.html',
        {'invader' : i}
    )

def invader_update(request, invader_id):
    return HttpResponse("You're updating invader %s." % invader_id)

def add_invader(request, city_id):
    c = get_object_or_404(City, pk=city_id)
    if c.invader_set.filter(name=request.POST['name']).count() > 0:
        return render(request, 'si/city.html', {'city': c, 'error_message': 'The Invader %s already exists!' % request.POST['name']})
    i = c.invader_set.create(name=request.POST['name'])
    i.save()
    return HttpResponseRedirect(reverse('invader_detail', args=(i.id,)))
