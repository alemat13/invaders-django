from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CityForm, InvaderForm
from .models import City, Invader


class IndexView(generic.ListView):
    model = City

class CityView(generic.DetailView):
    model = City

class InvaderView(generic.DetailView):
    model = Invader

class InvaderCreateView(CreateView):
    model = Invader
    fields = ['name', 'points', 'status', 'cp', 'city', 'comment', 'localisation', 'gmaps_url', 'latitude', 'longitude', 'flashed_by']

class InvaderUpdateView(UpdateView):
    model = Invader
    fields = '__all__'

class InvaderDeleteView(DeleteView):
    model = Invader
    success_url = reverse_lazy('invader-list')

def update_invader(request, invader_id):
    return HttpResponse("You're updating invader %s." % invader_id)

def add_invader(request, slug):
    c = get_object_or_404(City, slug=slug)
    if c.invader_set.filter(name=request.POST['name']).count() > 0:
        return render(request, 'si/city_detail.html', {'city': c, 'error_message': 'The Invader %s already exists!' % request.POST['name']})
    i = c.invader_set.create(name=request.POST['name'])
    i.save()
    return HttpResponseRedirect(reverse('invader_detail', args=(i.slug,)))

def invader_add(request):
    if request.method == 'POST':
        pass
    else:
        form = InvaderForm()
        return render(request, 'si/invader_form.html')

def add_city(request):
    if City.objects.filter(name=request.POST['name']).count() > 0:
        return render(request, 'si/city_list.html', {'error_message': 'This town, %s, already exists folk!' % request.POST['name']})
    c = City(name=request.POST['name'], prefix=request.POST['prefix'])
    c.save()
    return HttpResponseRedirect(reverse('city_detail', args=(c.slug,)))