from django.db import models

# Create your models here.

#class Energy(models.Model):
#	Node_number = models.CharField(max_length=10)
#	Tegangan = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#	Energy = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
#	Arus = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
#	Frekuensi = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#	Total_energy =  models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#	Waktu = models.DateTimeField(blank=True, null=True)


#	def __str__(self):
#		return self.Node_number

class Node(models.Model):
	Node_ID = models.CharField(max_length=10)


class NodeEnergy(models.Model):
	node = models.ForeignKey(Node, on_delete=models.CASCADE)
	Tegangan = models.CharField(max_length=100)
	Energy = models.CharField(max_length=100)
	Arus = models.CharField(max_length=100)
	Frekuensi = models.CharField(max_length=100)
	Total_energy = models.CharField(max_length=100)
	Waktu = models.CharField(max_length=100)
