#from django.shortcuts import render
# Create your views here.

from django.http import Http404
from django.shortcuts import render

from .models import Customer
from .models import EnergyData
from django.http import HttpResponse


def index(request):
    all_nodes = Customer.objects.all()
    context = {'all_nodes' : all_nodes}
    return render(request, 'energy/index.html', context)


def detail(request, node_id):
    return HttpResponse("<h2>Details for Customer id: " + str(node_id) + "</h2>")
