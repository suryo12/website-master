#from django.shortcuts import render
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.views.generic.base import TemplateView, View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import FormView
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.utils import formats, timezone
# Create your views here.

from .models import Attendance

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Attendance
from .serializers import AttendanceSerializer


class ListAttendanceView(TemplateView):
    template_name = 'absensi/list_attendance.html'

    def get_context_data(self, **kwargs):
        context_data = super(ListAttendanceView, self).get_context_data(**kwargs)

        all_attendance = Attendance.objects.all()
        context_data['all_attendance'] =  all_attendance
        return context_data


class APIAttendanceView(APIView):
	def get(self,request):
		all_attendance = Attendance.objects.all()
		serializer = AttendanceSerializer(all_attendance, many=True)
		return Response(serializer.data)

	def post(self,request, format=None):
		serializer = AttendanceSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

