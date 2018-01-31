from django.shortcuts import render, get_object_or_404
from .models import NodeID, Data
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import NodeIDSerializer
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.views.generic.base import TemplateView, View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import FormView
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.utils import formats, timezone
from django.contrib.auth import get_user_model
from django.http import JsonResponse

def index(request):
    all_nodes = NodeID.objects.all()
    context = {
        'all_nodes':all_nodes,
    }
    return render(request, 'landslide/index.html', context)

def detail(request, nodeid_id):
    nodeid = get_object_or_404(NodeID, id=nodeid_id)
    return render(request, 'landslide/detail.html', {'nodeid': nodeid})

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

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landslide/charts.html')

def get_data(request, *args, **kwargs):
    data = {}
    return JsonResponse(data)

class ChartData(APIView):

    def get(self, request, format=None):
        gs_count = User.objects.all().count()
        label = []
        teg = []
        for item in Data.objects.all() :
            if item.node_id.node_name == "Kaliurang1" :
                label.append(item.timestamp)
                teg.append(item.vibration)
        data = {
            "labels": label,
            "default": teg,
        }
        return JsonResponse(data)
