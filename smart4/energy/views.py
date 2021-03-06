#from django.shortcuts import render
# Create your views here.

from django.http import Http404
from django.shortcuts import render

from .models import Customer
from .models import EnergyData
from django.http import HttpResponse

#from django.template import loader

#from .serializers import AttendanceSerializer

def index(request):
    all_nodes = Customer.objects.all()
    context = {'all_nodes' : all_nodes}
    #return render(request, 'energy/index.html', {'all_energys': all_energys})
    return render(request, 'energy/index.html', context)
#    context = {'all_energys': all_energys}
#    return reader(request, 'energy/index.html', context)

def detail(request, node_id):
    #try:
    #    energy = Customer.objects.get(pk=Node_ID)
    #except Customer.DoesNotExist:
    #    raise Http404("Node does not exist")
    #return render(request, 'energy/detail.html', {'energy': energy})
    return HttpResponse("<h2>Details for Customer id: " + str(Node_ID) + "</h2>")
#    for energy in all_energys:
#        url = '/energy/' + str(energy.id) + '/'
#    html += '<a href="' + url + '">' + energy.Node_ID + '</a><br>'
#    return HttpResponse(html)

#def detail(request, Node_ID):
#    return HttpResponse("<h2>Detail for Node_ID: "+ str(Node_ID)+"</h2)")


#class ListEnergyView(TemplateView):
#    template_name = 'energy/list_energy.html'

#    def get_context_data(self, **kwargs):
#        context_data = super(ListEnergyView, self).get_context_data(**kwargs)

#        all_energy = Energy.objects.all()
#        context_data['all_energy'] =  all_energy
#        return context_data


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

