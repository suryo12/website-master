from .models import NodeID, Data
from datetime import datetime, date
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import NodeIDSerializer
from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Avg, Max, Min
import json

def IndexView(request):
    nodes = NodeID.objects.all()
    context = {
        'nodes' : nodes,
    }
    return render(request, 'smart/index.html', context)

def ChartCoba(request):
    nodes = NodeID.objects.all()
    context = {
        'nodes': nodes,
    }
    return render(request, 'smart/chart.html', context)
    #context_object_name = 'all_albums'

    #def get_queryset(self):
    #    return Album.objects.all()


def DetailView(request, node_id):
    now = datetime.now().date()
    #nodes = Data.objects.filter(node_id=node_id).filter(tanggal=now)
    nodes = Data.objects.filter(node_id=node_id).filter(tanggal=date(int(2018),int(1),int(23)))
    context = {
        'nodes': nodes
    }
    #print(node)
    return render(request, 'smart/tanggal.html', context)

def ChartDetail(request, node_id, tahun, bulan, hari):
    tanggal = datetime.now().date()
    #print(tanggal)
    tanggal = tanggal.replace(year=int(tahun), month=int(bulan), day=int(hari))
    #print(tanggal)
    date = Data.objects.filter(node_id=node_id, tanggal=tanggal)
    context = {
        'date' : date,
    }
    return render(request, 'smart/chartdetail.html', context)

class APINodeView(APIView):

    def get(self,request):
        all_nodes = Data.objects.all()
        serializer = NodeIDSerializer(all_nodes, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = NodeIDSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

User = get_user_model()


