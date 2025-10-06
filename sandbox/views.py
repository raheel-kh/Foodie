from django.shortcuts import render
from django.http import HttpResponse
from random import choice

# Create your views here.
def index(request):

    data = ["Cake", "Juice", "Shake", "Pasta", "Pizza"]
    context = {"foods" : data}
    return render(request, "sandbox/index.html" , context)