from django.shortcuts import render
from .models import Dog
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.
def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

class DogsList(ListView):
    model = Dog

class DogDetail(DetailView):
    model = Dog

class DogCreate(CreateView):
    model = Dog
    fields = '__all__' # or array of fields --> ['name', 'breed', 'age'] 

class DogUpdate(UpdateView):
    model = Dog
    fields = '__all__'
    
class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs/'

# def dogs_index(request):
#     dogs = Dog.objects.all()
#     return render(request, 'dogs/index.html', { 'dogs': dogs })

# def dogs_detail(request, dog_id):
#     dog = Dog.objects.get(id=dog_id)
#     return render(request, 'dogs/detail.html', { 'dog': dog })