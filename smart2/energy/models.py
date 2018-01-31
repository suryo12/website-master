from django.db import models

# Create your models here.
class Node(models.Model):
    Node_ID = models.CharField(max_length=10)
    Wilayah = models.CharField(max_length=100)

    def __str__(self):
	return self.Wilayah
#	def __str__(self):
#		return self.Node_number

class NodeEnergy(models.Model):
	node = models.ForeignKey(Node, on_delete=models.CASCADE)
	Tegangan = models.CharField(max_length=100)
	Energy = models.CharField(max_length=100)
	Arus = models.CharField(max_length=100)
	Frekuensi = models.CharField(max_length=100)
	Total_energy = models.CharField(max_length=100)
	Waktu = models.CharField(max_length=100)
