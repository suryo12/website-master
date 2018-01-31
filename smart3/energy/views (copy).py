#from django.shortcuts import render
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.views.generic.base import TemplateView, View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import FormView
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.utils import formats, timezone
# Create your views here.

from .models import Energy

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Energy
#from .serializers import AttendanceSerializer

#def index(request):
#    all_energys = Energy.objects.all()
#    html = ''
#    for energy in all_energys:
#        url = '/energy/' + str(energy.id) + '/'
#    html += '<a href="' + url + '">' + energy.Node_ID + '</a><br>'
#    return HttpResponse(html)

#def detail(request, Node_ID):
#    return HttpResponse("<h2>Detail for Node_ID: "+ str(Node_ID)+"</h2)")
class ListEnergyView(TemplateView):
    template_name = 'energy/list_energy.html'

    def get_context_data(self, **kwargs):
        context_data = super(ListEnergyView, self).get_context_data(**kwargs)

        all_energy = Energy.objects.all()
        context_data['all_energy'] =  all_energy
        return context_data


#class APIAttendanceView(APIView):
#	def get(self,request):
#		all_energy = Energy.objects.all()
#		serializer = EnergySerializer(all_energy, many=True)
#		return Response(serializer.data)

#	def post(self,request, format=None):
#		serializer = EnergySerializer(data=request.data)
#		if serializer.is_valid():
#			serializer.save()
#			return Response(serializer.data, status=status.HTTP_201_CREATED)
#		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




