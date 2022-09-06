from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
def index(request):
    return render(request, "home.html")

def index2(request):
    return render(request, "about.html")