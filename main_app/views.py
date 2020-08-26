from django.shortcuts import render

class Dog:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

dogs = [
    Dog("Meatball", "Cardigan Welsh Corgi", "Cuddly and full of energy", 2),
    Dog("Daisy", "Golden Retriever", "Lazy", 4),
]

# Create your views here.
def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', { 'dogs': dogs })