from django.shortcuts import render
# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Homie, Location
from .forms import HomieForm, SawForm

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def homies_index(request):
    homies = Homie.objects.all()
    return render(request, 'homies/index.html', { 'homies': homies })

def homies_detail(request, homie_id):
    homie_data = Homie.objects.get(id=homie_id)
    saw_homie_not = Saw.objects.exclude(id__in = homie_data.saw.all().values_list('id'))
    saw_form = SawForm()
    return render(request, 'homies/detail.html', { 
        'homie': homie_data,
        'saw_form': saw_form,
        'locations': locations_homie_not
    })

def assoc_location(request, homie_id, location_id):
    # The add method accepts both the whole model object or its ID for associations
    Homie.objects.get(id=homie_id).locations.add(location_id)
    return redirect('detail', homie_id=homie_id)

def add_saw(request, homie_id):
    form = SawForm(request.POST)
    if form.is_valid():
        new_saw = form.save(commit=False)
        new_saw.homie_id = homie_id
        new_saw.save()
    return redirect('detail', homie_id=homie_id)
    
def new_homie(request):
    if request.method == 'POST':
        form = HomieForm(request.POST)
        if form.is_valid():
            homie = form.save()
            return redirect('detail', homie.id)
    else:
        form = HomieForm()
    context = { 'form': form }
    return render(request, 'homies/homie_form.html', context)

def homies_update(request, homie_id):
    homie = Homie.objects.get(id=homie_id)
    if request.method == "POST":
        form = HomieForm(request.POST, instance=homie)
        if form.is_valid():
            homie = form.save()
            return redirect('detail', homie.id)
    else: 
        form = HomieForm(instance=homie)
    return render(request, 'homies/homie_form.html', { 'form': form })

def homies_delete(request, homie_id):
    pass

#FOR LOCATOIN 
# To view all locations made
def location_index(request):
    locations = Location.objects.all()
    print(locations)
    return render(request, 'main_app/location_list.html', { 'locations': locations })

class LocationDetail(DetailView):
  model = Location

# To create a location
class LocationCreate(CreateView):
  model = Location
  fields = '__all__'

# To update a location
class LocationUpdate(UpdateView):
  model = Location
  fields = ['name', 'color']

# To delete a location
class LocationDelete(DeleteView):
  model = Location
  success_url = '/locations/'
