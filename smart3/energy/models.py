import os
from django.db import models


# Create your models here.

class Energy(models.Model): #customer
	Node_ID = models.AutoField(primary_key=True)
	Nama = models.CharField(max_length=64)
	No_Telp = models.CharField(max_length=64)
#    Alamat = models.CharField(max_length=64)
#data=energydata

	def __str__(self):
		return self.Nama + '-' + self.No_Telp

class NodeEnergy(models.Model): #energydata
	node = models.ForeignKey(Energy, on_delete=models.CASCADE)
	Tegangan = models.CharField(max_length=1000)
	Energy = models.CharField(max_length=1000)
	Arus = models.CharField(max_length=1000)
	Frekuensi = models.CharField(max_length=1000)
	Total_energy = models.CharField(max_length=1000)
	Waktu = models.CharField(max_length=1000)
#defaultnya none
	def __str__(self):
		return self.Tegangan + '-' + self.Arus
