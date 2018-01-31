#from django.shortcuts import render

# Create your views here.

#from django.shortcuts import render
#from django.contrib.humanize.templatetags.humanize import naturaltime
#from django.views.generic.base import TemplateView, View
#from django.utils.decorators import method_decorator
#from django.views.decorators.csrf import csrf_exempt
#from django.views.generic.edit import FormView
#from django.http.response import HttpResponse, HttpResponseBadRequest
#from django.utils import formats, timezone
# Create your views here.

#from .models import Energy

#from django.shortcuts import render
#from django.shortcuts import get_object_or_404

#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status
#from .models import Energy
#from .serializers import AttendanceSerializer


#class ListEnergyView(TemplateView):
#    template_name = 'energy/list_energy.html'

#    def get_context_data(self, **kwargs):
#        context_data = super(ListEnergyView, self).get_context_data(**kwargs)

#        all_energy = Energy.objects.all()
#        context_data['all_energy'] =  all_energy
#        return context_data
